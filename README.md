[![Validate services (schema + build)](https://github.com/bethantimmins/data-service-catalog/actions/workflows/validate.yml/badge.svg)](https://github.com/bethantimmins/data-service-catalog/actions/workflows/validate.yml)

# Data Service Catalog (Open Source Starter)

A curated, open-source **Data Service Catalog** built with code-first metadata, automatic validation, and a lightweight web viewer.

---

## 📖 About

This repository helps teams build and maintain a consistent, discoverable catalog of data services. Each service is described in **YAML**, validated by schema, and surfaced via a static site hosted on GitHub Pages.

Think of it as a **self-updating directory** of your organization's data services—keep it accurate and accessible with minimal effort.

---

## 🚀 Quick Start (for Contributors)

### 1. Add or update a service
Copy and customize a file from `services/`, e.g.:

```bash
cp services/customer_orders.yml services/my_new_service.yml
```

Update fields like `name`, `description`, `owner`, `status`, `access`, `tags`, and anything else relevant.

### 2. Run validations (optional but highly recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
export RUAMEL_NO_EXTENSIONS=1
pip install -r requirements.txt
./tools/validate.sh
python3 -m http.server 8000  # then open http://localhost:8000/docs/
```

### 3. Push changes & open a Pull Request

- Create a PR against `main`.
- The **Validate services** workflow will run automatically.
- Once it passes, you’re good to merge!

---

## 📂 Project Structure

```
services/           # Service-specific YAML definitions
catalog.schema.json # Validation schema for services
tools/validate.sh   # Runs validation + builds catalog.json
build/catalog.json  # Generated metadata (do not edit by hand)
docs/               # Serves as the GitHub Pages site
scripts/            # Python logic behind validation and generation
```

---
## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute, add/edit services, and validate your changes.

We also provide structured templates to make contributing smoother:

- 🐞 [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) → for reporting reproducible issues
- ✨ [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) → for proposing new ideas or improvements
- ❓ [Question](.github/ISSUE_TEMPLATE/question.md) → for asking clarifying questions
- 📥 [Pull Request Template](.github/pull_request_template.md) → used automatically when opening a PR

Please follow these to help us keep contributions clear and consistent.

---
## 🧪 Examples   👈 ***add this right here***

New here? Start by looking at these examples:

- **Good example** → [examples/good_service.yaml](examples/good_service.yaml)
- **Bad example** → [examples/bad_service.yaml](examples/bad_service.yaml)

Use the *good* example as a template for creating new service files.  
Compare it with the *bad* example to help spot common mistakes!

**How to add a new service**
1. Copy `examples/good_service.yaml` into the `services/` folder and rename it (e.g. `services/my-service.yaml`).
2. Fill in the fields (making sure they match the allowed schema values).
3. Open a Pull Request—your CI will automatically validate your file before it goes live!
   
---
## 🔐 Security

If you find a security vulnerability, please review our [SECURITY.md](SECURITY.md) for how to report it responsibly.  
⚠️ Do **not** open a public GitHub issue for security reports.

---
## 🔑 For Maintainers

- **Update `catalog.schema.json`** when adding or changing metadata fields.
- **Review PRs carefully**, ensuring metadata stays consistent and validation is green.
- **Encourage contributors** to run validations locally before creating PRs.

---

## 📜 License & Conduct

- This project is released under the **MIT License**. See `LICENSE`.
- All contributors must adhere to the [Code of Conduct](CODE_OF_CONDUCT.md).

---

> This repo is modern, open, and made to grow—thank you for helping make metadata shine! Great to go under the hood? Try adding a new service—you’re in the driver’s seat!
