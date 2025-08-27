# Contributing to Data Service Catalog

Welcome! 👋  
This repo publishes a **code-first data service catalogue**: each service is described in YAML, validated in CI, and rendered to a simple website (GitHub Pages).

---

## 🚀 Quick Start

- **Small change?** Edit files in the GitHub UI and open a Pull Request (PR).
- **Add a service?** Copy an existing file in `services/`, update fields, then open a PR.
- **Validation is automatic** → GitHub Actions will run checks for you.

---

## 🗂 How the repo works

- **Service metadata** → `services/*.yml`
- **Schema definition** → `catalog.schema.json` (defines required/optional fields)
- **Validation** → `tools/validate.sh` builds `build/catalog.json`
- **Website** → files in `docs/`, auto-published to  
  👉 <https://bethantimmins.github.io/data-service-catalog/>

A PR cannot be merged if validation fails (schema errors or broken build).

---

## ✍️ Add or update a service

1. Duplicate an existing YAML in `services/`:
2. Fill in the fields (examples):
- `name`: **Customer Orders Service**
- `description`: Short, clear description
- `owner`: Team name
- `status`: Active / Deprecated / Planned
- `sources`: URLs or upstream systems
- `schema_uri`: optional pointer to Avro/JSON schema
- `access`: how to consume (API, table, etc.)
- `update_frequency`: real-time / hourly / daily
- `business_purpose`: why it exists
- `kpis`: list of key metrics
- `quality`: e.g. `freshness_sla_min`, `completeness_target_pct`
- `sensitivity`: Public / Internal / Restricted
- `compliance`: GDPR / CCPA / etc.
- `sla`: availability guarantees
- `monitoring`: dashboards, alerting
- `support`: contact
- `tags`: labels for discovery
- `code_object`: pipeline module (if any)

3. Commit to a **new branch** and open a PR.

---

## ✅ Validation

This repo uses a GitHub Action:  
**Validate services (schema + build)**

It ensures:
- All YAML matches `catalog.schema.json`
- A valid `build/catalog.json` is generated

If validation fails:
- Click into the Action run → see exact error & file/line
- Fix locally or in the GitHub editor
- Push changes → checks re-run automatically

---

## 🛠 Run locally (optional)

You don’t need to run locally — CI will catch issues.  
But if you want to preview before pushing:

### Setup
```bash
./tools/validate.sh
python3 -m venv .venv
source .venv/bin/activate

# Avoid compiler prompts on macOS
export RUAMEL_NO_EXTENSIONS=1

pip install -r requirements.txt
