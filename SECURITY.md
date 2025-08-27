# Security Policy

We take the security of **Data Service Catalog** seriously and appreciate responsible reports.

## Supported Versions

We aim to fix security issues in the **latest main branch** and the most recent tagged release.
If you are using an older version, please upgrade before reporting unless the issue prevents upgrading.

## Reporting a Vulnerability

Please email **bethan@organa.com.au** with the subject line `SECURITY: <short description>` and include:

- A clear description of the issue and **impact**
- **Steps to reproduce** (or a minimal proof-of-concept)
- Affected version/commit and environment details
- Suggested fixes or mitigations (if known)
- Whether the report is **public** anywhere

> ⚠️ **Do not** open public GitHub issues for security reports.

## Preferred Disclosure Process

1. Report privately via email.
2. We will acknowledge receipt within **3 business days**.
3. We will investigate and aim to provide a remediation plan or status update within **7 business days**.
4. Once a fix is ready and released, we’ll coordinate a **responsible disclosure** with you.

## Scope

- Source code and configuration in this repository
- Build and validation workflows (e.g., schema validation, CI)

Out of scope (unless they directly affect this project):

- Third‑party dependencies (please report upstream)
- Social engineering, spam, or non-technical issues
- Denial of Service without a clear, reproducible bug

## Handling Secrets

If you encounter credentials or secrets in files or logs:
- **Do not** use them.
- **Do not** share them.
- Immediately notify us privately so we can revoke/rotate.

## Temporary Mitigations

If a simple mitigation exists (config, docs, or validation rule), feel free to propose it in your report or open a private PR reference in your email.

## Credits

We are happy to **credit reporters** in release notes, unless you prefer to remain anonymous.
