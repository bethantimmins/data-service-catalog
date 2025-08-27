import os, sys, json, glob, yaml
from jsonschema import validate, ValidationError

def main():
        # Resolve schema path relative to the repo root
    this_dir = os.path.dirname(os.path.abspath(__file__))           # .../scripts
    repo_root = os.path.dirname(this_dir)                           # go up to repo root
    schema_path = os.path.join(repo_root, "schemas", "catalog.schema.json")

    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"Schema not found at: {schema_path}")

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    files = sys.argv[1:] or glob.glob("services/*.yml")
    if not files:
        print("No YAML files found in services/*.yml")
        sys.exit(1)

    ok = True
    for f in files:
        try:
            data = yaml.safe_load(open(f))
            validate(instance=data, schema=schema)
            print(f"✅ {f} is valid")
        except FileNotFoundError:
            print(f"❌ {f}: file not found"); ok = False
        except ValidationError as e:
            print(f"❌ {f}: schema validation failed\n   -> {e.message}")
            ok = False
        except Exception as e:
            print(f"❌ {f}: {e}")
            ok = False
    sys.exit(0 if ok else 2)

if __name__ == "__main__":
    main()
