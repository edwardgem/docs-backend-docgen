#!/usr/bin/env python3
"""Build a first OpenAPI draft from route inventory."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except Exception:
    yaml = None

def _function_name_to_summary(function_name: str) -> str:
    """Convert a snake_case function name to a human-readable summary."""
    if not function_name:
        return "API Operation"
    return " ".join(word.capitalize() for word in function_name.replace("-", "_").split("_"))

TAG_DESCRIPTIONS = {
    "Agent Lifecycle": "Agent registration, launch, polling, and lifecycle operations.",
    "Dashboard": "Dashboard-facing APIs (generally non-customer integration surface).",
    "Frontend Shell": "Frontend SPA shell routes.",
    "Log Proxy": "Agent log ingestion and proxy APIs.",
    "LLM Utilities": "Prompt classification and utility APIs.",
    "Ops Utilities": "Operational refresh/streaming utility APIs.",
    "Presence": "User presence and heartbeat APIs.",
    "HITL": "Human-in-the-loop routing and decision APIs.",
    "RLHF": "RLHF policy, runtime, and decision management APIs.",
    "User Profile": "End-user profile management APIs.",
    "Worktray": "Worktray-facing interactive APIs.",
    "Workitems": "Work item queue and status APIs for human review.",
    "Auth / Sessions": "Authentication and session-related APIs.",
    "Admin / Ops": "Administrative and operator APIs.",
    "Analytics": "Analytics and dashboard query APIs.",
    "Internal": "Internal service-to-service APIs.",
    "Uncategorized": "Routes pending category assignment.",
}

_FLASK_PATH_PARAM_RE = re.compile(r"<(?:(?P<converter>[^:>]+):)?(?P<name>[^>]+)>")
_PREFERRED_HANDLER_BY_PATH_METHOD = {
    ("/api/alp/agents/{name}/instances/{instance_id}/hitl-callback", "post"): "alp_hitl_callback",
}


def _slug(text: str) -> str:
    cleaned = []
    for ch in text:
        if ch.isalnum():
            cleaned.append(ch.lower())
        else:
            cleaned.append("_")
    s = "".join(cleaned)
    while "__" in s:
        s = s.replace("__", "_")
    return s.strip("_")


def _schema_for_converter(converter: str | None) -> dict[str, Any]:
    kind = (converter or "").strip().lower()
    if kind in {"int", "integer"}:
        return {"type": "integer"}
    if kind in {"float"}:
        return {"type": "number", "format": "float"}
    if kind in {"uuid"}:
        return {"type": "string", "format": "uuid"}
    return {"type": "string"}


def _normalize_flask_path(path: str) -> tuple[str, list[dict[str, Any]]]:
    raw = str(path or "").strip()
    params: list[dict[str, Any]] = []

    def repl(match: re.Match[str]) -> str:
        converter = match.group("converter")
        name = (match.group("name") or "").strip()
        if not name:
            return "{}"
        params.append(
            {
                "name": name,
                "in": "path",
                "required": True,
                "schema": _schema_for_converter(converter),
            }
        )
        return "{" + name + "}"

    converted = _FLASK_PATH_PARAM_RE.sub(repl, raw)
    return converted, params


def _make_operation(route: dict[str, Any], method: str, openapi_path: str, path_params: list[dict[str, Any]]) -> dict[str, Any]:
    method_lc = method.lower()
    function_name = route.get("function_name") or ""
    summary = _function_name_to_summary(function_name)
    op_id = f"{method_lc}_{_slug(function_name or 'route')}_{_slug(openapi_path)}"

    operation: dict[str, Any] = {
        "summary": summary,
        "description": "",
        "operationId": op_id,
        "tags": route.get("tags") or ["Uncategorized"],
        "responses": {
            "200": {
                "description": "Success"
            },
            "400": {
                "description": "Bad request"
            },
            "401": {
                "description": "Unauthorized"
            },
            "500": {
                "description": "Server error"
            }
        },
        "x-source": {
            "file": route.get("source_file"),
            "function": route.get("function_name"),
            "line": route.get("line"),
        },
        "x-audience": route.get("audience", "public"),
    }
    if path_params:
        operation["parameters"] = path_params

    internal = route.get("audience") == "internal"
    if not internal:
        operation["security"] = [
            {"ApiKeyAuth": []},
            {"SessionToken": []}
        ]

    return operation


def _build_spec(inventory: dict[str, Any], include_audiences: set[str] | None = None) -> dict[str, Any]:
    routes = inventory.get("routes", [])
    source = inventory.get("source", "")

    paths: dict[str, Any] = {}
    tags_used = set()

    collisions: list[dict[str, Any]] = []
    resolved_collisions: list[dict[str, Any]] = []

    for route in routes:
        flask_path = route.get("path")
        if not flask_path:
            continue

        audience = str(route.get("audience") or "public").strip().lower()
        if include_audiences is not None and audience not in include_audiences:
            continue

        openapi_path, path_params = _normalize_flask_path(flask_path)
        route["source_file"] = source
        methods = route.get("methods") or ["GET"]
        path_item = paths.setdefault(openapi_path, {})
        for method in methods:
            method_lc = str(method).lower()
            next_operation = _make_operation(route, method, openapi_path, path_params)
            if method_lc in path_item:
                existing = path_item[method_lc]
                preferred = _PREFERRED_HANDLER_BY_PATH_METHOD.get((openapi_path, method_lc))
                existing_fn = (existing.get("x-source") or {}).get("function")
                next_fn = (next_operation.get("x-source") or {}).get("function")
                if preferred and next_fn == preferred and existing_fn != preferred:
                    path_item[method_lc] = next_operation
                    resolved_collisions.append(
                        {
                            "path": openapi_path,
                            "method": method_lc,
                            "reason": "preferred_handler_override",
                            "preferred_function": preferred,
                            "replaced_function": existing_fn,
                        }
                    )
                    continue
                if preferred and existing_fn == preferred:
                    resolved_collisions.append(
                        {
                            "path": openapi_path,
                            "method": method_lc,
                            "reason": "preferred_handler_kept",
                            "preferred_function": preferred,
                            "dropped_function": next_fn,
                        }
                    )
                    continue
                collisions.append(
                    {
                        "path": openapi_path,
                        "method": method_lc,
                        "kept_operationId": existing.get("operationId"),
                        "dropped_operationId": next_operation.get("operationId"),
                        "kept_function": (existing.get("x-source") or {}).get("function"),
                        "dropped_function": (next_operation.get("x-source") or {}).get("function"),
                    }
                )
                continue
            path_item[method_lc] = next_operation

        for tag in route.get("tags") or []:
            tags_used.add(tag)

    tags = [
        {
            "name": t,
            "description": TAG_DESCRIPTIONS.get(t, "")
        }
        for t in sorted(tags_used)
    ]

    spec: dict[str, Any] = {
        "openapi": "3.0.3",
        "info": {
            "title": "AMP API",
            "version": "1.0",
            "description": (
                "REST API for the AMP (Autonomous Multi-agent Platform). "
                "Integrate your agents with AMP to get transparency, accountability, "
                "and human oversight (HITL) for governed AI agent operations."
            ),
        },
        "servers": [
            {"url": "https://api.amp.example.com", "description": "Production (placeholder)"},
            {"url": "http://localhost:5000", "description": "Local development"},
        ],
        "tags": tags,
        "paths": dict(sorted(paths.items())),
        "components": {
            "securitySchemes": {
                "ApiKeyAuth": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "X-API-Key",
                },
                "SessionToken": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "X-Session-Token",
                },
            },
            "schemas": {
                "ErrorResponse": {
                    "type": "object",
                    "properties": {
                        "error": {"type": "string"},
                        "detail": {"type": "string"},
                    },
                }
            }
        },
    }
    if collisions:
        spec["x-route-collisions"] = collisions
    if resolved_collisions:
        spec["x-route-collisions-resolved"] = resolved_collisions
    return spec


def _yaml_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "":
        return "''"
    needs_quote = any(ch in text for ch in [":", "#", "{", "}", "[", "]", ",", "&", "*", "?", "|", ">", "%", "@", "`", "\"", "'"]) or text.strip() != text
    if needs_quote:
        return json.dumps(text, ensure_ascii=True)
    return text


def _to_yaml_lines(obj: Any, indent: int = 0) -> list[str]:
    pad = " " * indent
    if isinstance(obj, dict):
        lines: list[str] = []
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                lines.append(f"{pad}{key}:")
                lines.extend(_to_yaml_lines(value, indent + 2))
            else:
                lines.append(f"{pad}{key}: {_yaml_scalar(value)}")
        return lines or [f"{pad}{{}}"]
    if isinstance(obj, list):
        lines = []
        if not obj:
            return [f"{pad}[]"]
        for item in obj:
            if isinstance(item, (dict, list)):
                lines.append(f"{pad}-")
                lines.extend(_to_yaml_lines(item, indent + 2))
            else:
                lines.append(f"{pad}- {_yaml_scalar(item)}")
        return lines
    return [f"{pad}{_yaml_scalar(obj)}"]


def _dump_yaml(obj: Any) -> str:
    if yaml is not None:
        return yaml.safe_dump(obj, sort_keys=False, allow_unicode=False)
    return "\n".join(_to_yaml_lines(obj)) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build draft OpenAPI from extracted routes")
    parser.add_argument("--inventory", required=True, help="Path to routes inventory JSON")
    parser.add_argument("--yaml-out", required=True, help="Path to OpenAPI YAML output")
    parser.add_argument("--json-out", required=True, help="Path to OpenAPI JSON output")
    parser.add_argument(
        "--audiences",
        default="public,partner,internal",
        help="Comma-separated route audiences to include (e.g. public or public,partner)",
    )
    args = parser.parse_args()

    inv_path = Path(args.inventory).resolve()
    yaml_out = Path(args.yaml_out).resolve()
    json_out = Path(args.json_out).resolve()

    inventory = json.loads(inv_path.read_text(encoding="utf-8"))
    include_audiences = {a.strip().lower() for a in str(args.audiences).split(",") if a.strip()}
    spec = _build_spec(inventory, include_audiences=include_audiences)

    yaml_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.parent.mkdir(parents=True, exist_ok=True)

    yaml_out.write_text(_dump_yaml(spec), encoding="utf-8")
    json_out.write_text(json.dumps(spec, indent=2), encoding="utf-8")

    path_count = len(spec.get("paths", {}))
    op_count = sum(len(v.keys()) for v in spec.get("paths", {}).values())

    print(f"Wrote OpenAPI YAML: {yaml_out}")
    print(f"Wrote OpenAPI JSON: {json_out}")
    collisions = spec.get("x-route-collisions", [])
    resolved = spec.get("x-route-collisions-resolved", [])
    print(f"Paths: {path_count}")
    print(f"Operations: {op_count}")
    print(f"Collisions: {len(collisions)}")
    print(f"Resolved collisions: {len(resolved)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
