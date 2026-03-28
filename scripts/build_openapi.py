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

_ACRONYMS = {"sse", "hitl", "rlhf", "llm", "api", "id", "url"}

def _function_name_to_summary(function_name: str) -> str:
    """Convert a snake_case function name to a human-readable summary."""
    if not function_name:
        return "API Operation"
    words = []
    for word in function_name.replace("-", "_").split("_"):
        if word.lower() in _ACRONYMS:
            words.append(word.upper())
        else:
            words.append(word.capitalize())
    return " ".join(words)

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

# Endpoint-specific wording overrides for customer-facing clarity.
# Keep this map small and only use it where function-name summaries/docstrings
# are too generic for external docs.
_OPERATION_OVERRIDES: dict[tuple[str, str], dict[str, Any]] = {
    (
        "/api/hitl/request",
        "post",
    ): {
        "summary": "HITL Request",
        "description": (
            "Submit a HITL request and optionally register a completion callback.\n\n"
            "AMP-HITL evaluates WHEN/WHO/WHAT/WHERE and either returns `no-hitl` "
            "immediately or accepts the request and completes later via human or auto routing."
        ),
        "requestBody": {
            "required": True,
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "required": ["caller_id", "instance_id", "org_id", "agent_name"],
                        "properties": {
                            "caller_id": {"type": "string", "description": "Canonical HITL correlation ID."},
                            "instance_id": {"type": "string", "description": "Alias of caller_id for compatibility."},
                            "org_id": {"type": "string"},
                            "agent_name": {"type": "string"},
                            "rlhf": {
                                "type": "object",
                                "description": "RLHF/policy evaluation inputs for this HITL request.",
                                "properties": {
                                    "policy_values_source": {
                                        "type": "string",
                                        "enum": ["external", "internal"],
                                    },
                                    "action_context": {
                                        "type": "object",
                                        "additionalProperties": True,
                                    },
                                    "facts_context": {
                                        "type": "object",
                                        "additionalProperties": True,
                                    },
                                    "criteria": {
                                        "type": "array",
                                        "items": {"type": "object", "additionalProperties": True},
                                    },
                                    "evidence": {"type": "object", "additionalProperties": True},
                                    "run_mode": {"type": "string"},
                                    "sim_run_id": {"type": "string"},
                                    "sim_time": {"type": "string"},
                                    "checkpoint_id": {"type": "string"},
                                },
                            },
                            "hitl": {
                                "type": "object",
                                "properties": {
                                    "enable": {"type": "boolean"},
                                    "when": {"type": "string"},
                                    "who": {"type": "string"},
                                    "what": {"type": "string", "enum": ["approval", "notify"]},
                                    "where": {"type": "string", "enum": ["amp", "email"]},
                                },
                            },
                            "callback": {
                                "type": "object",
                                "properties": {
                                    "url": {"type": "string", "format": "uri"},
                                    "secret": {"type": "string"},
                                    "timeout_ms": {"type": "integer", "minimum": 500, "maximum": 30000},
                                },
                                "required": ["url"],
                            },
                        },
                    },
                    "example": {
                        "caller_id": "invoice-payment-agent-5c58-20260310135042",
                        "instance_id": "invoice-payment-agent-5c58-20260310135042",
                        "org_id": "O-0011-ST20251201090030",
                        "agent_name": "invoice-payment-agent-5c58",
                        "rlhf": {
                            "policy_values_source": "external",
                            "action_context": {
                                "action_type": "approve_payment",
                                "resource_type": "invoice",
                                "resource_id": "invoice-payment-agent-5c58-20260310135042",
                            },
                            "facts_context": {
                                "amount_over_threshold": True,
                            },
                            "criteria": [
                                {"criterion_id": "c_amount_within_policy", "result": True},
                                {"criterion_id": "c_vendor_risk_acceptable", "result": True},
                            ],
                        },
                        "hitl": {
                            "enable": True,
                            "when": "amount > 1000",
                            "who": "initiator",
                            "what": "approval",
                            "where": "amp",
                        },
                        "callback": {
                            "url": "https://caller.example.com/hitl/callback",
                            "secret": "shared-secret",
                            "timeout_ms": 5000,
                        },
                    },
                }
            },
        },
        "responses": {
            "200": {
                "description": "No HITL needed or HITL disabled.",
                "content": {
                    "application/json": {
                        "example": {
                            "status": "no-hitl",
                            "information": "WHEN condition not met",
                        }
                    }
                },
            },
            "202": {
                "description": "Accepted for asynchronous HITL processing.",
                "content": {
                    "application/json": {
                        "example": {
                            "status": "waiting-for-response",
                            "caller_id": "invoice-payment-agent-5c58-20260310135042",
                            "information": {
                                "who": "initiator@example.com",
                                "what": "approval",
                                "where": "amp",
                            },
                            "links": {
                                "status": "/api/hitl/status?caller_id=invoice-payment-agent-5c58-20260310135042",
                            },
                        }
                    }
                },
            },
            "400": {
                "description": "Validation or preflight error.",
                "content": {
                    "application/json": {
                        "example": {
                            "status": "error",
                            "error": "callback_url_invalid_scheme",
                            "information": "callback URL must use http or https",
                        }
                    }
                },
            },
        },
    },
    (
        "/api/hitl/get-decision",
        "get",
    ): {
        "summary": "HITL Get Decision",
        "description": "Poll normalized HITL decision state for a caller/activity ID.",
        "parameters": [
            {
                "name": "caller_id",
                "in": "query",
                "required": False,
                "schema": {"type": "string"},
                "description": "Canonical HITL correlation ID.",
            },
            {
                "name": "instance_id",
                "in": "query",
                "required": False,
                "schema": {"type": "string"},
                "description": "Alias of caller_id (use either one).",
            },
        ],
        "responses": {
            "200": {
                "description": "Decision state found or still pending.",
                "content": {
                    "application/json": {
                        "examples": {
                            "pending": {
                                "value": {
                                    "caller_id": "invoice-payment-agent-5c58-20260310135042",
                                    "status": "pending",
                                }
                            },
                            "complete_human": {
                                "value": {
                                    "caller_id": "invoice-payment-agent-5c58-20260310135042",
                                    "status": "complete",
                                    "resolution": "approve",
                                    "method": "human",
                                    "workitem_id": "invoice-payment-agent-5c58-20260310135042-20260314013057",
                                    "information": "approved by reviewer",
                                }
                            },
                            "complete_auto": {
                                "value": {
                                    "caller_id": "invoice-payment-agent-5c58-20260310135042",
                                    "status": "complete",
                                    "resolution": "approve",
                                    "method": "auto",
                                    "workitem_id": "",
                                    "information": "auto decision recorded; workitem not created",
                                }
                            },
                        }
                    }
                },
            }
        },
    },
}

# Deprecated public aliases we intentionally hide from generated docs.
# Canonical HITL endpoints are under /api/hitl/*.
_HIDDEN_PATH_PREFIXES = (
    "/api/hitl-agent",
)


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
    override = _OPERATION_OVERRIDES.get((openapi_path, method_lc), {})
    op_id = f"{method_lc}_{_slug(function_name or 'route')}_{_slug(openapi_path)}"

    operation: dict[str, Any] = {
        "summary": override.get("summary", summary),
        "description": override.get("description", route.get("description") or ""),
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

    if "requestBody" in override:
        operation["requestBody"] = override["requestBody"]

    if "parameters" in override:
        operation["parameters"] = override["parameters"]

    if "responses" in override and isinstance(override["responses"], dict):
        for code, response in override["responses"].items():
            operation["responses"][str(code)] = response

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
        if any(openapi_path.startswith(prefix) for prefix in _HIDDEN_PATH_PREFIXES):
            continue
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
    needs_quote = "\n" in text or any(ch in text for ch in [":", "#", "{", "}", "[", "]", ",", "&", "*", "?", "|", ">", "%", "@", "`", "\"", "'"]) or text.strip() != text
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
