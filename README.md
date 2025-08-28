# Data Service Catalog

[![Validate services](https://github.com/bethantimmins/data-service-catalog/actions/workflows/validate.yml/badge.svg)](https://github.com/bethantimmins/data-service-catalog/actions/workflows/validate.yml)
[![Publish catalog](https://github.com/bethantimmins/data-service-catalog/actions/workflows/publish-catalog.yml/badge.svg)](https://github.com/bethantimmins/data-service-catalog/actions/workflows/publish-catalog.yml)

A simple, lightweight service catalog for data teams.  
Service definitions live in YAML, get validated, and are published to a JSON file served on GitHub Pages.

👉 Live site: [bethantimmins.github.io/data-service-catalog](https://bethantimmins.github.io/data-service-catalog/)

---

## 👩‍💻 For Users (Fork & Run)

Want to run your own catalog?

1. **Fork this repository** into your own GitHub account.  
2. Add your service YAMLs under `services/`.  
3. Push changes to your fork.  
   - GitHub Actions will validate your YAML and publish `docs/catalog.json`.  
   - Enable GitHub Pages on your fork → you’ll get your own live catalog site.  

---

## 🤝 For Contributors (Improving the project)

This repository also serves as a reference/example for building catalogs.

- Example services in `services/` are illustrative — they are not meant to be a canonical source.  
- Contributions welcome: schema changes, tooling improvements, docs, fixes.  
- Workflow for contributing:  
  1. Create a feature branch from `main`.  
  2. Add/update files (schemas, tools, docs, example YAMLs).  
  3. Open a Pull Request.  
- Do **not** manually edit `docs/catalog.json`. Automation handles that.  
- See also: [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and issue/PR templates under `.github/`.  

---

## 🛠 For Maintainers (Admins of this repo)

Maintainers keep the demo repo healthy:

- `main` is protected by a ruleset requiring:  
  - `validate-services-pr` (schema validation + build on PRs)  
  - `publish-catalog-pr` (catalog publishing workflow on PRs)  
- Every change goes through two PRs:  
  1. A contributor PR (services/schema/docs).  
  2. A bot PR (`chore: publish updated catalog.json`) which syncs `docs/catalog.json`.  
- Merge both for the Pages site to stay current.  
- Housekeeping:  
  - Delete merged branches.  
  - Keep GitHub Pages enabled.  
  - Watch for bot PRs and merge them once checks pass.  

---

## 🚀 Quick Start (Local Dev)

For contributors and maintainers:

1. **Install dependencies**  
   ```bash
   python -m pip install -r requirements.txt
   ```

2. **Run validation locally**  
   ```bash
   bash tools/validate.sh
   ```

   - Validates YAML against `schemas/service.schema.json`.  
   - Builds `build/catalog.json`.  

CI will always run validation, but local runs help debug faster.

---

## 🧭 How it Works

1. Service YAML files live in `services/`  
2. They are validated against `schemas/service.schema.json`  
3. A JSON catalog is built under `build/catalog.json`  
4. CI copies it to `docs/catalog.json` (via **publish-catalog** workflow)  
5. GitHub Pages serves it at the project website  

---

## 🧹 Housekeeping

- Feature branches are deleted once their PRs are merged.  
- Bot PRs (`chore: publish updated catalog.json`) are expected → merge them.  
- If validation fails, run `bash tools/validate.sh` locally to debug.  

---

## 📂 Repo Structure

```
services/          # Service YAML definitions
schemas/           # JSON Schema for validation
docs/              # Published JSON catalog + Pages site
tools/             # Validation scripts
.github/workflows  # CI workflows (validate + publish)
.github/ISSUE_TEMPLATE/  # GitHub issue templates
.github/PULL_REQUEST_TEMPLATE.md # PR template
SECURITY.md        # Security policy
CONTRIBUTING.md    # Contribution guidelines
```

---



---

## 🔄 Workflow Overview

```
┌──────────────┐
│  services/   │   (YAML definitions)
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Validate   │   (validate-services-pr job)
│   schema +   │
│   build      │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Build      │   (catalog.json generated)
│   catalog    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Publish     │   (publish-catalog-pr job)
│  docs/       │
│  catalog.json│
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   GitHub     │   (Pages site auto-updates)
│   Pages site │
└──────────────┘
```

---

## 🛠 Troubleshooting

- **PR shows “Expected — waiting for status to be reported”**  
  - Ruleset requires a stale check.  
  - Fix: Settings → Rulesets → Main branch protections → remove stale checks → re-add live job names (`validate-services-pr`, `publish-catalog-pr`).  

- **Bot PR (`chore: publish updated catalog.json`) doesn’t appear**  
  - Ensure the change touched `services/*.yml`.  
  - Check `GH_BOT_TOKEN` exists in repo secrets.  
  - If missing, manually re-run **Publish catalog** workflow in Actions.  

- **Catalog PR stuck because branch is behind main**  
  - Open the bot PR → click **Update branch** (or “Bring branch up to date”).  
  - Rerun checks.  

- **Validation fails**  
  - Run locally with:  
    ```bash
    bash tools/validate.sh
    ```  
  - Fix YAML errors and push again.  

---

## 🙌 Contributing

- Fork for your own use.  
- PRs welcome for improvements to schema, docs, or tooling.  
- Read [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.  
- Read [SECURITY.md](SECURITY.md) for vulnerability reporting.  
