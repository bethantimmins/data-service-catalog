import json, importlib, pkgutil
from pathlib import Path

def test_generate_catalog(tmp_path, monkeypatch):
    # Ensure build dir is isolated
    build_dir = tmp_path / "build"
    monkeypatch.chdir(Path(__file__).resolve().parents[1])
    # Import all pipelines to register
    import pipelines
    for m in pkgutil.iter_modules(pipelines.__path__):
        importlib.import_module(f"pipelines.{m.name}")
    # Now read generated catalog (module atexit hook writes it)
    catalog_path = Path("build/catalog.json")
    assert catalog_path.exists()
    data = json.loads(catalog_path.read_text())
    assert isinstance(data, list) and len(data) >= 1
    assert any("name" in s and "access" in s for s in data)
