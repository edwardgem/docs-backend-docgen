#!/usr/bin/env python3
"""
Generate OpenAPI outputs and sync public YAML into docs-amp-api.

Default flow:
1) make generate        (docs-backend-docgen)
2) make check           (docs-backend-docgen)
3) copy output/openapi.public.yaml -> ../docs-amp-api/openapi/v1.yaml
4) make check           (docs-amp-api)

Optional:
- commit synced file in docs-amp-api (--commit-message ...)
- push docs-amp-api commit (--push)
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> None:
    print(f"[run] ({cwd}) {' '.join(cmd)}")
    subprocess.run(cmd, cwd=str(cwd), check=True)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync docs-backend-docgen public OpenAPI output to docs-amp-api."
    )
    parser.add_argument(
        "--docs-amp-api-root",
        default=None,
        help="Path to docs-amp-api repo (default: ../docs-amp-api).",
    )
    parser.add_argument(
        "--skip-generate",
        action="store_true",
        help="Skip `make generate` in docs-backend-docgen.",
    )
    parser.add_argument(
        "--skip-check",
        action="store_true",
        help="Skip `make check` in docs-backend-docgen.",
    )
    parser.add_argument(
        "--skip-docs-check",
        action="store_true",
        help="Skip `make check` in docs-amp-api after copy.",
    )
    parser.add_argument(
        "--commit-message",
        default=None,
        help="If provided, commit docs-amp-api/openapi/v1.yaml with this message.",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Push docs-amp-api changes after commit.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    docs_amp_root = (
        Path(args.docs_amp_api_root).resolve()
        if args.docs_amp_api_root
        else (repo_root.parent / "docs-amp-api").resolve()
    )

    source_yaml = repo_root / "output" / "openapi.public.yaml"
    dest_yaml = docs_amp_root / "openapi" / "v1.yaml"

    if not args.skip_generate:
        run(["make", "generate"], cwd=repo_root)
    if not args.skip_check:
        run(["make", "check"], cwd=repo_root)

    if not source_yaml.exists():
        print(f"[error] Source file missing: {source_yaml}")
        return 1
    if not docs_amp_root.exists():
        print(f"[error] docs-amp-api repo not found: {docs_amp_root}")
        return 1

    dest_yaml.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source_yaml, dest_yaml)
    print(f"[sync] {source_yaml} -> {dest_yaml}")

    if not args.skip_docs_check:
        run(["make", "check"], cwd=docs_amp_root)

    if args.commit_message:
        run(["git", "add", "openapi/v1.yaml"], cwd=docs_amp_root)
        run(["git", "commit", "-m", args.commit_message], cwd=docs_amp_root)
        if args.push:
            run(["git", "push", "origin", "main"], cwd=docs_amp_root)

    print("[done] Sync completed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as e:
        print(f"[error] Command failed with exit code {e.returncode}")
        raise SystemExit(e.returncode)
