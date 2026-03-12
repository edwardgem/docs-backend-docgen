#!/usr/bin/env python3
"""Sanity checks for generated route inventory + OpenAPI draft."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Check docgen outputs")
    parser.add_argument("--inventory", required=True, help="routes_inventory.json")
    parser.add_argument("--openapi", required=True, help="openapi.draft.json")
    parser.add_argument("--max-uncategorized", type=int, default=999999, help="Fail if uncategorized routes exceed this")
    parser.add_argument("--allow-collisions", action="store_true", help="Allow route collisions")
    args = parser.parse_args()

    inv = json.loads(Path(args.inventory).read_text(encoding="utf-8"))
    spec = json.loads(Path(args.openapi).read_text(encoding="utf-8"))

    route_count = int(inv.get("route_count", 0))
    uncategorized = int((inv.get("tag_counts") or {}).get("Uncategorized", 0))
    paths = spec.get("paths") or {}
    path_count = len(paths)
    op_count = sum(len(item) for item in paths.values())
    collisions = spec.get("x-route-collisions") or []

    print(f"route_count={route_count}")
    print(f"uncategorized={uncategorized}")
    print(f"path_count={path_count}")
    print(f"operation_count={op_count}")
    print(f"collisions={len(collisions)}")

    errors: list[str] = []
    if uncategorized > args.max_uncategorized:
        errors.append(f"uncategorized_exceeds_limit: {uncategorized} > {args.max_uncategorized}")
    if collisions and not args.allow_collisions:
        errors.append(f"route_collisions_detected: {len(collisions)}")

    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1

    print("check=ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
