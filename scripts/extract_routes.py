#!/usr/bin/env python3
"""Extract Flask routes from amp-backend app.py into an inventory."""

from __future__ import annotations

import argparse
import ast
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DEFAULT_METHODS = ["GET"]


@dataclass
class RouteRecord:
    path: str
    methods: list[str]
    function_name: str
    line: int
    tags: list[str]
    audience: str


def _safe_literal(node: ast.AST) -> Any:
    try:
        return ast.literal_eval(node)
    except Exception:
        return None


def _normalize_methods(raw_methods: Any) -> list[str]:
    if not raw_methods:
        return DEFAULT_METHODS[:]
    methods: list[str] = []
    if isinstance(raw_methods, (list, tuple, set)):
        for item in raw_methods:
            text = str(item).strip().upper()
            if text:
                methods.append(text)
    if not methods:
        return DEFAULT_METHODS[:]
    return sorted(set(methods))


def _categorize(path: str) -> tuple[list[str], str]:
    p = (path or "").strip()
    audience = "public"

    if p in {"/api/login", "/api/register", "/api/password/change", "/api/password/setup", "/api/logout"}:
        return ["Auth / Sessions"], audience
    if p.startswith("/api/password"):
        return ["Auth / Sessions"], audience
    if p.startswith("/api/config"):
        return ["Auth / Sessions"], audience

    if p in {"/", "/<path:path>"}:
        return ["Frontend Shell"], "internal"
    if p.startswith("/api/internal/"):
        audience = "internal"
        return ["Internal"], audience
    if p.startswith("/api/admin/"):
        return ["Admin / Ops"], "partner"
    if p.startswith("/api/dashboard/"):
        return ["Dashboard"], "partner"
    if p.startswith("/api/amp/chat"):
        return ["Dashboard"], "partner"
    if p.startswith("/api/amp/refresh-events") or p.startswith("/api/amp/sse-status") or p.startswith("/api/amp/trigger-refresh"):
        return ["Ops Utilities"], "partner"
    if p.startswith("/api/worktray/chat"):
        return ["Worktray"], "partner"
    if p.startswith("/api/presence/"):
        return ["Presence"], "partner"
    if p.startswith("/api/classify_intent") or p.startswith("/api/llm/classify"):
        return ["LLM Utilities"], "partner"
    if p.startswith("/api/settings/api-key"):
        return ["Auth / Sessions"], "partner"
    if p.startswith("/api/user/profile"):
        return ["User Profile"], "partner"
    if p.startswith("/api/rlhf/"):
        if p.startswith("/api/rlhf/test/") or p.startswith("/api/rlhf/jobs/enqueue") or p.startswith("/api/rlhf/stage_tick/trigger") or p.startswith("/api/rlhf/status"):
            return ["RLHF"], "partner"
        return ["RLHF"], audience
    if p.startswith("/api/workitems"):
        return ["Workitems", "HITL"], audience
    if p.startswith("/api/hitl-agent"):
        return ["HITL"], audience
    if p.startswith("/api/log"):
        return ["Log Proxy"], audience
    if p.startswith("/api/analytics/"):
        return ["Analytics"], audience
    if p.startswith("/api/agent-tasks") or p.startswith("/api/agent/start") or p.startswith("/api/agent/"):
        return ["Agent Lifecycle"], audience
    if p.startswith("/api/alp/"):
        return ["Agent Lifecycle"], audience
    if p.startswith("/api/agents/") or p == "/api/agents":
        return ["Agent Lifecycle"], audience
    if p.startswith("/api/init_agent") or p.startswith("/api/abort"):
        return ["Agent Lifecycle"], audience
    return ["Uncategorized"], audience


def _extract_routes(app_file: Path) -> list[RouteRecord]:
    tree = ast.parse(app_file.read_text(encoding="utf-8"), filename=str(app_file))
    results: list[RouteRecord] = []

    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue

        for deco in node.decorator_list:
            if not isinstance(deco, ast.Call):
                continue
            func = deco.func
            if not isinstance(func, ast.Attribute):
                continue
            if func.attr != "route":
                continue

            path = ""
            if deco.args:
                raw_path = _safe_literal(deco.args[0])
                if isinstance(raw_path, str):
                    path = raw_path

            methods = DEFAULT_METHODS[:]
            for kw in deco.keywords:
                if kw.arg == "methods":
                    methods = _normalize_methods(_safe_literal(kw.value))

            if not path:
                continue

            tags, audience = _categorize(path)
            results.append(
                RouteRecord(
                    path=path,
                    methods=methods,
                    function_name=node.name,
                    line=node.lineno,
                    tags=tags,
                    audience=audience,
                )
            )

    dedup = {}
    for r in results:
        key = (r.path, tuple(r.methods), r.function_name)
        dedup[key] = r

    records = sorted(dedup.values(), key=lambda x: (x.path, x.function_name, x.line))
    return records


def _to_json(records: list[RouteRecord], source_file: Path) -> dict[str, Any]:
    tag_counts: dict[str, int] = {}
    audience_counts: dict[str, int] = {}
    for record in records:
        for tag in record.tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
        audience_counts[record.audience] = audience_counts.get(record.audience, 0) + 1

    return {
        "source": str(source_file),
        "route_count": len(records),
        "tag_counts": dict(sorted(tag_counts.items())),
        "audience_counts": dict(sorted(audience_counts.items())),
        "routes": [
            {
                "path": r.path,
                "methods": r.methods,
                "function_name": r.function_name,
                "line": r.line,
                "tags": r.tags,
                "audience": r.audience,
            }
            for r in records
        ],
    }


def _to_markdown(payload: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# AMP Route Inventory (Draft)")
    lines.append("")
    lines.append(f"- Source: `{payload['source']}`")
    lines.append(f"- Route count: **{payload['route_count']}**")
    lines.append("")
    lines.append("## Tag Counts")
    for tag, count in payload.get("tag_counts", {}).items():
        lines.append(f"- `{tag}`: {count}")
    lines.append("")
    lines.append("## Audience Counts")
    for audience, count in payload.get("audience_counts", {}).items():
        lines.append(f"- `{audience}`: {count}")
    lines.append("")
    lines.append("## Routes")
    lines.append("")
    lines.append("| Path | Methods | Tags | Audience | Function | Line |")
    lines.append("|---|---|---|---|---|---:|")
    for r in payload.get("routes", []):
        methods = ", ".join(r.get("methods", []))
        tags = ", ".join(r.get("tags", []))
        lines.append(
            f"| `{r.get('path')}` | `{methods}` | `{tags}` | `{r.get('audience')}` | `{r.get('function_name')}` | {r.get('line')} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract Flask route inventory from app.py")
    parser.add_argument("--app-file", required=True, help="Path to amp-backend app.py")
    parser.add_argument("--json-out", required=True, help="Output path for route inventory JSON")
    parser.add_argument("--md-out", required=True, help="Output path for route inventory Markdown")
    args = parser.parse_args()

    app_file = Path(args.app_file).resolve()
    json_out = Path(args.json_out).resolve()
    md_out = Path(args.md_out).resolve()

    records = _extract_routes(app_file)
    payload = _to_json(records, app_file)

    json_out.parent.mkdir(parents=True, exist_ok=True)
    md_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    md_out.write_text(_to_markdown(payload), encoding="utf-8")

    print(f"Wrote JSON: {json_out}")
    print(f"Wrote Markdown: {md_out}")
    print(f"Routes extracted: {payload['route_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
