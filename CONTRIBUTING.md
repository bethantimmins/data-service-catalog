 Contributing to Data Service Catalog

🎉 First off, thanks for taking the time to contribute! Your help makes this project better for everyone.

This guide outlines how to contribute, the workflow we follow, and a few best practices.

---

## 🛠 Getting Started

1. **Fork the repo** on GitHub.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/data-service-catalog.git
   ```
3. **Create a branch** for your change:
   ```bash
   git checkout -b feature/my-new-service
   ```
4. Install dependencies (if any are required):
   ```bash
   pip install -r requirements.txt
   ```

---

## 💡 How to Contribute

We welcome contributions in many forms:
- Adding or updating services in `catalog.json`.
- Improving validation or schema rules.
- Enhancing the documentation or examples.
- Fixing bugs or suggesting improvements.
- Opening issues for bugs, questions, or feature ideas.

---

## 🔎 Validation & Checks

Every contribution is automatically validated by **GitHub Actions**:
- **Schema validation**: Ensures `catalog.json` follows the defined format.
- **Build check**: Confirms files and docs render correctly.
- **Pages deployment**: Makes sure the catalog is published.

✅ Make sure your branch passes these checks before opening a Pull Request.

---

## 📝 Commit Guidelines

We use a simple, structured commit message format:

```
type: short description
```

Where `type` can be:
- `feat`: a new feature
- `fix`: a bug fix
- `docs`: documentation updates
- `chore`: repository setup, CI/CD, or non-feature changes

Examples:
```
feat: add new Customer Orders service
fix: correct schema validation error
docs: update README with quickstart guide
```

---

## 🔀 Pull Requests

1. Push your branch to your fork.
2. Open a **Pull Request** against the `main` branch.
3. Make sure:
   - Your PR passes all validation checks.
   - The PR description clearly explains the change.
   - Linked issues (if any) are referenced (e.g. `Closes #12`).

We encourage small, focused PRs — easier to review and merge quickly!

---

## 🐛 Issues

- Use issues to report bugs, request features, or ask questions.
- Before opening a new issue, please check if it already exists.
- Include clear steps to reproduce bugs if reporting one.

---

## 🤝 Community Guidelines

- Be kind and respectful to others.
- Offer constructive feedback.
- Remember that this project is open source and built by volunteers.

For more, see our [Code of Conduct](CODE_OF_CONDUCT.md).

---

💡 **Tip:** If you’re new to open source, check out GitHub’s [first contributions guide](https://github.com/firstcontributions/first-contributions).

---

Thanks again for contributing! 🚀


