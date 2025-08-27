#!/usr/bin/env bash
set -euo pipefail

# Run schema validation + build JSON into build/catalog.json
python3 scripts/validate_yaml.py
