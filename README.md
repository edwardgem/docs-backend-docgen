# docs-backend-docgen

Milestone 1 bootstrap for AMP API documentation generation.

This repo provides two scripts:

1. `scripts/extract_routes.py`
- Parses Flask `@app.route(...)` decorators from `amp-backend/app.py`.
- Produces a normalized route inventory JSON + Markdown summary.

2. `scripts/build_openapi.py`
- Converts route inventory into a first OpenAPI draft (`openapi.draft.yaml` + `.json`).
- Applies initial category tags (`Log Proxy`, `HITL`, `RLHF`, etc.).
- Supports audience filtering:
  - `public,partner,internal` (default, full draft)
  - `public` (customer-facing publish artifact)

3. `scripts/check_outputs.py`
- Runs sanity checks on generated artifacts (uncategorized count, route collisions).

## Quick Start

```bash
cd /Users/edwardc/Projects/docs-backend-docgen
make generate
make check
```

Equivalent direct commands:

```bash
cd /Users/edwardc/Projects/docs-backend-docgen
python3 scripts/extract_routes.py \
  --app-file /Users/edwardc/Projects/amp-backend/app.py \
  --json-out output/routes_inventory.json \
  --md-out output/routes_inventory.md

python3 scripts/build_openapi.py \
  --inventory output/routes_inventory.json \
  --yaml-out output/openapi.draft.yaml \
  --json-out output/openapi.draft.json

python3 scripts/check_outputs.py \
  --inventory output/routes_inventory.json \
  --openapi output/openapi.draft.json \
  --allow-collisions
```

## Outputs

- `output/routes_inventory.json`
- `output/routes_inventory.md`
- `output/openapi.draft.yaml`
- `output/openapi.draft.json`
- `output/openapi.public.yaml`
- `output/openapi.public.json`

## Notes

- This is a **draft generator** for rapid coverage, not final hand-authored API docs.
- Internal endpoints are flagged with `x-audience: internal` based on path rules.
- Partner/ops endpoints are flagged with `x-audience: partner` and excluded from `openapi.public.*`.
- Flask route params are normalized to OpenAPI params:
  - `/api/items/<id>` -> `/api/items/{id}`
  - `/api/files/<path:filename>` -> `/api/files/{filename}`
- Next milestone can add strict schema modeling and examples per operation.
