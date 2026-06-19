# Release Readiness Notes

Use this file to capture the final review after the docs-drift patch.

- Corrected command: `docs-drift-demo --status`
- Files changed: `README.md`
- Checks performed: confirm `pyproject.toml` exposes the `docs-drift-demo` console script and `src/docs_drift_demo/cli.py` accepts `--status`.
- Reviewer notes: keep the repair focused on the stale command instead of rewriting unrelated README sections.
