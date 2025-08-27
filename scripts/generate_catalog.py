import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import importlib, pkgutil
from lib.catalog import dump_catalog
import pipelines

# Import all modules in pipelines package to trigger decorators
for m in pkgutil.iter_modules(pipelines.__path__):
    importlib.import_module(f"pipelines.{m.name}")

dump_catalog("build/catalog.json")
print("Generated build/catalog.json")
