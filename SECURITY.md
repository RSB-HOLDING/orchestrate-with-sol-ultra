# Security Policy

## Supported version

Security fixes are considered for the current `main` branch. No released version or long-term-support branch exists yet.

## Report privately

Do not open a public issue for a vulnerability, leaked credential, private prompt, personal data, or sensitive repository detail.

Use GitHub’s private vulnerability-reporting form:

<https://github.com/RSB-HOLDING/orchestrate-with-sol-ultra/security/advisories/new>

Include:

- A concise description and potential impact.
- The affected file and commit.
- Reproduction steps or a minimal example.
- Any relevant host, model, or Codex surface.
- Suggested mitigation, if known.

Remove real credentials, customer data, and unnecessary private content. The maintainers will coordinate validation, remediation, and disclosure with the reporter. There is currently no guaranteed response-time SLA.

## Relevant security issues

Examples include instructions that:

- Expand authority beyond the user’s request.
- Permit silent external writes, spending, deployment, signing, or publication.
- Expose secrets or sensitive content to undeclared workers or providers.
- Allow unsafe concurrent writes in a shared checkout.
- Bypass required verification or misrepresent unproven work as complete.
- Create a practical prompt-injection path through untrusted repository content.

General model mistakes, unsupported performance claims, and ordinary documentation defects can use the public issue forms when they contain no sensitive information.
