import sys, json, glob, yaml
from jsonschema import validate, ValidationError

def main():
    schema = json.load(open("catalog.schema.json"))
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
