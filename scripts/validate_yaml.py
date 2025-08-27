# scripts/validate_yaml.py
import os, sys, glob, json
import yaml
from jsonschema import validate, ValidationError

def main():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(this_dir)  # .../data-service-catalog
    schema_path = os.path.join(repo_root, "schemas", "catalog.schema.json")

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    # Pick up BOTH .yml and .yaml, deterministic order
    yml = glob.glob(os.path.join(repo_root, "services", "*.yml"))
    yaml_ = glob.glob(os.path.join(repo_root, "services", "*.yaml"))
    files = sorted(yml + yaml_)

    if not files:
        print("No YAML files found in services/")
        # still write an empty array so the site shows the 'no services yet' state
        out_dir = os.path.join(repo_root, "build")
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "catalog.json"), "w", encoding="utf-8") as f:
            json.dump([], f, indent=2)
        return

    # Validate and collect
    services = []
    for path in files:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        try:
            validate(instance=data, schema=schema)
        except ValidationError as e:
            print(f"Schema validation FAILED for {os.path.relpath(path, repo_root)}")
            print(e.message)
            sys.exit(2)

        services.append(data)

    # Write build/catalog.json
    out_dir = os.path.join(repo_root, "build")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "catalog.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(services, f, indent=2, ensure_ascii=False)

    print(f"Wrote {out_path} with {len(services)} service(s).")

if __name__ == "__main__":
    main()
