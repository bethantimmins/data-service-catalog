#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."  # ensure repo root

echo
echo "=== Validating service YAML files against catalog.schema.json ==="
python3 scripts/validate_yaml.py

echo
echo "=== Importing pipelines to register services and generate build/catalog.json ==="
python3 -m scripts.generate_catalog
echo "✅ Catalog written to build/catalog.json"
