# Daytona Docs Drift Demo

This tiny repository is used by the Daytona guide to practice a docs-drift repair workflow with Omni Engineer and Claude Engineer.

## Start the demo

```bash
python run.py --serve
```

## Expected output

The command should print a short status line for the demo service.

## Exercise

The README intentionally contains a command that no longer matches the package entry point. Use an AI engineer to compare the documentation with the code, patch the README, and record the release-readiness checks in `docs/release-readiness.md`.
