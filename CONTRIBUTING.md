# Git Workflow — signed-evidence-pipeline

A quick reference for how to interact with `main` and manage local work on this repo.

## Core principle

Never commit directly to `main`. Even solo, treat `main` as the "known good" branch — every change goes through a branch and a Pull Request first. This also lets CI/CD checks (checkov/tfsec/gitleaks) run *before* anything lands on `main`, not after.

## Workflow

### 1. Sync main before starting new work
```bash
git checkout main
git pull origin main
```

### 2. Create a feature branch
```bash
git checkout -b feature/vpc-networking
```
Naming convention:
- `feature/x` — new functionality
- `fix/x` — bug fixes
- `chore/x` — maintenance (deps, docs, cleanup)

### 3. Work and commit incrementally
```bash
git add terraform/vpc.tf
git commit -m "Add VPC module with public/private subnet split"
```
Commit messages should describe what and why, briefly. Avoid vague messages like "wip" or "updates."

### 4. Push the branch
```bash
git push -u origin feature/vpc-networking
```
The `-u` sets up tracking so future `git push`/`git pull` on this branch work without extra flags.

### 5. Open a Pull Request on GitHub
Go to the repo on GitHub — a "Compare & pull request" prompt appears for the branch you just pushed. Add a short description of what the branch does. This is where CI/CD checks run automatically.

### 6. Review, let checks pass, then merge
- Wait for GitHub Actions checks to pass
- Review the "Files changed" tab yourself before merging — catches stray `.tfvars`, debug lines, etc.
- Use **Squash and merge** for a clean `main` history (collapses work-in-progress commits into one clean commit on `main`; full history stays on the branch)

### 7. Sync back and clean up
```bash
git checkout main
git pull origin main
git branch -d feature/vpc-networking
```

## Day-to-day habits

- Local `main` should mirror GitHub's `main` — only pull into it, don't edit on it directly
- Check which branch you're on before editing: `git status` or `git branch` (current branch marked with `*`)
- If you accidentally start editing on `main`: `git stash`, create/switch to the right branch, `git stash pop` to recover your changes

## Before your first commit

Confirm `.gitignore` is actually catching `.tfstate`, `.tfvars`, and `.terraform/`. Right after your first `terraform init`/`plan`, run `git status` — none of those files should appear as untracked. If `.gitignore` is working, they won't show up in the list at all.