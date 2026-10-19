# mergeflow-sandbox

Prototype repo (steward) for the agentic dev-flow trial: **GitHub native merge queue + jj + CodeRabbit**.
Not for real work. See the trial notes in the COS-platform brief.

## What's wired
- `ci` check runs on both `pull_request` and `merge_group` (the merge-queue event).
- `main` is protected: PRs only, `ci` required, merge queue ON.
