# Code-First Data Service Catalogue

A lightweight, **code-first metadata pattern** for data teams. Describe each data service or pipeline in a small YAML file, register it via a decorator, validate in CI, and publish a machine-readable catalogue.

> **Why?** Discoverability, governance, and reuse — without heavy platforms or manual wikis.

## ✨ Features
- In-repo YAML per service (human-friendly, versioned)
- **Decorator** registers metadata from code at import time
- **JSON Schema** validation (CI + pre-commit)
- Auto-generate `build/catalog.json` for portals or downstream catalogs
- Example pipeline and schema to copy-paste

## 🚀 Quickstart
```bash
git clone <your-fork-url>
cd data-service-catalog-oss-starter
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
bash tools/validate.sh
cat build/catalog.json
```

## 🧱 Project Layout
```
services/           # YAML descriptors (one per service)
schemas/            # Interface/data schemas (Avro/OpenAPI/etc.)
lib/                # Catalog decorator & telemetry helpers
pipelines/          # Example pipeline(s) that register services
tools/              # CI/validation scripts
scripts/            # Helpers to build the catalog
tests/              # Minimal tests
.github/            # CI, issue + PR templates
docs/               # Optional docs site content
```

## 🛠 Define a Service
Create `services/customer_orders.yml` and fill it out. Then decorate your pipeline:

```python
from lib.catalog import register_service

@register_service("services/customer_orders.yml")
def customer_orders_pipeline(run_date=None):
    # your ETL/ELT logic here
    return "ok"
```

## 🧪 Validate & Build
```bash
bash tools/validate.sh    # validate YAML and emit build/catalog.json
pytest -q                  # optional tests
```

## 📦 Integrate Elsewhere
- Publish `build/catalog.json` to S3/GCS/Blob storage
- Feed it into **DataHub** / **OpenMetadata** with a small emitter
- Render a simple UI (docs/ includes a minimal HTML viewer example)

## 🔒 Notes
- The example entries use **placeholders** (e.g., domains like `example.com`). Replace with your real endpoints.
- Avoid committing secrets. See `.gitignore` suggestions below.

## 📄 License
Apache-2.0 (see `LICENSE`).

---

### README Badges (optional)
Add these once you enable Actions & Releases:
```
![CI](https://img.shields.io/github/actions/workflow/status/<owner>/<repo>/ci.yml?branch=main)
![License](https://img.shields.io/badge/license-Apache--2.0-blue)
![SemVer](https://img.shields.io/badge/semver-yes-brightgreen)
```
