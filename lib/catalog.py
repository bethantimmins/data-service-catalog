import json, yaml, pathlib, atexit

CATALOG_REGISTRY = []

def register_service(meta_path: str):
    """
    Decorator that registers a data service from a YAML metadata file.
    Attaches the parsed metadata to the function as `_catalog` and
    stores a registry record for later export.
    """
    def decorator(fn):
        meta = yaml.safe_load(pathlib.Path(meta_path).read_text())
        record = {**meta, "code_object": f"{fn.__module__}.{fn.__name__}"}
        CATALOG_REGISTRY.append(record)
        setattr(fn, "_catalog", record)
        return fn
    return decorator

def dump_catalog(path="build/catalog.json"):
    """Write the in-memory registry to disk as JSON."""
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(CATALOG_REGISTRY, indent=2))

# Optional auto-dump at interpreter exit in CLI/CI contexts
atexit.register(dump_catalog)
