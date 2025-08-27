#!/usr/bin/env python3
import os, sys, glob, json
from pathlib import Path
import yaml
from jsonschema import validate, ValidationError

# Make path resolution rock-solid both locally and in GitHub Actions
_ws = os.getenv("GITHUB_WORKSPACE")
REPO_ROOT = Path(_ws) if _ws else Path(__file__).resolve().parents[1]

SCHEMA_PATH = REPO_ROOT / "schemas" / "catalog.schema.json"
SERVICES_GLOBS = [
    str(REPO_ROOT / "services" / "*.yml"),
    str(REPO_ROOT / "services" / "*.yaml"),
]
BUILD_DIR = REPO_ROOT / "build"
BUILD_JSON = BUILD_DIR / "catalog.json"

def load_json(p: Path):
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

def load_yaml(p: Path):
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def main():
    # 1) Schema
    if not SCHEMA_PATH.exists():
        print(f"ERROR: Schema not found at {SCHEMA_PATH}", file=sys.stderr)
        sys.exit(1)
    schema = load_json(SCHEMA_PATH)

    # 2) Find service files (yml + yaml)
    service_files = []
    for g in SERVICES_GLOBS:
        service_files.extend(sorted(glob.glob(g)))

    if not service_files:
        print("No YAML files found under services/*.yml or *.yaml", file=sys.stderr)
        sys.exit(1)

    print("=== Validating service YAML files against schemas/catalog.schema.json ===")
    print("Found files:")
    for p in service_files:
        rel = os.path.relpath(p, REPO_ROOT)
        print(f" - {rel}")

    # 3) Validate and collect
    all_valid = True
    services = []

    for p in service_files:
        rel = os.path.relpath(p, REPO_ROOT)
        try:
            data = load_yaml(Path(p))
            validate(instance=data, schema=schema)
            print(f"✅ {rel} is valid")
            services.append(data)
        except ValidationError as e:
            all_valid = False
            print(f"❌ {rel}: schema validation failed")
            print(f"   -> {e.message}")

    if not all_valid:
        print("One or more service files failed validation. Aborting.", file=sys.stderr)
        sys.exit(2)

    # 4) Write a single aggregated JSON array
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    with BUILD_JSON.open("w", encoding="utf-8") as f:
        json.dump(services, f, indent=2, ensure_ascii=False)

    print(f"\nGenerated {os.path.relpath(BUILD_JSON, REPO_ROOT)} with {len(services)} services.")

if __name__ == "__main__":
    main()
