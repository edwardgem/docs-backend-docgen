APP_FILE ?= /Users/edwardc/Projects/amp-backend/app.py
OUT_DIR ?= output

INVENTORY_JSON := $(OUT_DIR)/routes_inventory.json
INVENTORY_MD := $(OUT_DIR)/routes_inventory.md
OPENAPI_JSON := $(OUT_DIR)/openapi.draft.json
OPENAPI_YAML := $(OUT_DIR)/openapi.draft.yaml
OPENAPI_PUBLIC_JSON := $(OUT_DIR)/openapi.public.json
OPENAPI_PUBLIC_YAML := $(OUT_DIR)/openapi.public.yaml

.PHONY: generate extract openapi openapi-public check sync-docs-amp-api clean

generate: extract openapi openapi-public

extract:
	python3 scripts/extract_routes.py \
		--app-file $(APP_FILE) \
		--json-out $(INVENTORY_JSON) \
		--md-out $(INVENTORY_MD)

openapi:
	python3 scripts/build_openapi.py \
		--inventory $(INVENTORY_JSON) \
		--yaml-out $(OPENAPI_YAML) \
		--json-out $(OPENAPI_JSON)

openapi-public:
	python3 scripts/build_openapi.py \
		--inventory $(INVENTORY_JSON) \
		--yaml-out $(OPENAPI_PUBLIC_YAML) \
		--json-out $(OPENAPI_PUBLIC_JSON) \
		--audiences public

check:
	python3 scripts/check_outputs.py \
		--inventory $(INVENTORY_JSON) \
		--openapi $(OPENAPI_JSON) \
		--allow-collisions

sync-docs-amp-api:
	python3 scripts/sync_docs_amp_api.py

clean:
	rm -f $(INVENTORY_JSON) $(INVENTORY_MD) $(OPENAPI_JSON) $(OPENAPI_YAML) $(OPENAPI_PUBLIC_JSON) $(OPENAPI_PUBLIC_YAML)
