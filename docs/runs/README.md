# Runs Log

One folder per model (kebab-case slug), containing every run for that model:docs/runs/<model-slug>/
├── <YYYY-MM-DD>-baseline/ ← TMDL export, committed before any write
└── <YYYY-MM-DD>.md ← audit + plan + (if applied) results for that run
Each run report contains: model name, baseline commit reference, changes
applied (per `PBI-*`), verification result, and outstanding manual items -- per
the "Run log" section in `.github/copilot-instructions.md`.

Each run happens on its own branch (`assessment/<model-slug>-<date>` for
read-only audits, `fix/<model-slug>-<date>` for runs that apply changes),
merged into `main` via PR. The branch is disposable; this folder is the
permanent record -- see "Branching convention" in `TASKS.md`.
