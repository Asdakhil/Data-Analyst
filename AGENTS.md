# AGENTS.md

## Mission

This repo is an older public analytics experiment repo. Keep changes focused on making it understandable, runnable, or safely archived.

## Safe Defaults

- Do not commit private datasets, credentials, or local machine paths.
- Prefer documentation and dependency cleanup before adding features.
- Rename files only in a dedicated cleanup task so links and notebook references can be checked.
- If converting this into a portfolio repo, add sample data or clear placeholder instructions.

## Suggested Organization

```text
streamlit_apps/
notebooks/
scripts/
data_samples/
README.md
requirements.txt
```

## Validation

For Streamlit scripts, run the target app locally and record the command used.

For notebooks, restart the kernel and run all cells when practical, or document why that was not possible.
