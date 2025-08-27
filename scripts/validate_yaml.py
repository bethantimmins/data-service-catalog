# scripts/validate_yaml.py
import os
import sys
import json
import glob
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, ValidationError

def repo_root() -> Path:
    # works whether run from repo root or tools/ or scripts/
    return Path(__file__).resolve().parent.parent

def load_schema(schema_path: Path) -> dict:
    with schema_path.open("r", encoding="utf-8") as f:
        return json.load(f)

def load_yaml(p: Path) -> dict:
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def main() -> int:
    root = repo_root()
    services_dir = root / "services"
    schema_path = root / "schemas" / "catalog.schema.json"
    build_dir = root / "build"
    output_path = build_dir / "catalog.json"

    if not services_dir.exists():
        print(f"ERROR: services directory not found at {services_dir}")
        return 2
    if not schema_path.exists():
        print(f"ERROR: schema not found at {schema_path}")
        return 2

    schema = load_schema(schema_path)
    validator = Draft202012Validator(schema)

    service_files = sorted(services_dir.glob("*.yml"))
    if not service_files:
        print("No YAML files found in services/. Nothing to validate.")
        # still create an empty catalog to keep Pages happy
        build_dir.mkdir(parents=True, exist_ok=True)
        output_path.write_text("[]", encoding="utf-8")
        return 0

    print(f"==> Validating service YAML files against {schema_path.name}")
    ok, bad = [], []

    for p in service_files:
        try:
            data = load_yaml(p)
            if data is None:
                raise ValueError("YAML file is empty")
            if not isinstance(data, dict):
                raise ValueError("Top-level YAML must be an object (mapping)")

            # Validate against JSON Schema
            errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
            if errors:
                msg = "; ".join(
                    f"{'/'.join(map(str, e.path)) or '<root>'}: {e.message}" for e in errors
                )
                raise ValidationError(msg)

            ok.append((p, data))
            print(f"  ✅ {p.relative_to(root)} is valid")

        except Exception as e:
            bad.append((p, str(e)))
            print(f"  ❌ {p.relative_to(root)} failed validation: {e}")

    # If any invalid, fail the job after reporting everything
    if bad:
        print("\nOne or more service definitions failed validation:")
        for p, msg in bad:
            print(f"  - {p.relative_to(root)}: {msg}")
        return 2

    # Write combined catalog (array of objects)
    build_dir.mkdir(parents=True, exist_ok=True)
    combined = [entry for _, entry in ok]
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(combined, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\nWrote {len(combined)} services to {output_path.relative_to(root)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
