# Daytona Docs Drift Demo

This tiny repository is used by the Daytona guide to practice a docs-drift repair workflow with Omni Engineer and Claude Engineer.

## Start the demo

```bash
docs-drift-demo --status
```

## Expected output

The command prints a short status line for the demo service:

```text
Daytona docs-drift demo: ready
```

## Exercise

The `docs-drift-start` branch intentionally contains an older command that no longer matches the package entry point. Use an AI engineer to compare the documentation with the code, patch the README, and record the release-readiness checks in `docs/release-readiness.md`.
