# 🛠️ Git Setup & Best Practices Guide

## ✍️ Git Configuration Basics

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

This configures your global identity and sets `main` as the default branch for new repos.

---

## 💡 Essential Git Concepts & Commands

### 📥 `git stash`

* Temporarily stores changes without committing them
* Useful for switching branches without losing work

```bash
git stash       # Save current changes
git stash pop   # Reapply and remove from stash
```

### 📩 `git pull`

* Downloads and merges changes from the remote

```bash
git pull origin main
```

### 🚀 `git push`

* Uploads local commits to the remote

```bash
git push origin main
```

### 🔀 `git merge`

* Combines changes from one branch into another, preserving commit history

```bash
git checkout main
git merge feature-branch
```

### 🎯 `git rebase`

* Reapplies commits on top of another base branch, creating a linear history

```bash
git checkout feature-branch
git rebase main
```

### 🔄 Other Useful Commands

| Command      | Description                                      |
| ------------ | ------------------------------------------------ |
| `git log`    | View commit history                              |
| `git status` | Check status of working directory                |
| `git diff`   | View unstaged changes                            |
| `git add`    | Stage file(s)                                    |
| `git reset`  | Unstage or undo commits                          |
| `git revert` | Safely undo changes by creating a reverse commit |

---

## 🌿 Branch Naming Conventions

### 📌 Why Commit Messages Matter

Clear, structured Git commit messages:
- Help collaborators understand changes
- Enable changelog generation
- Facilitate semantic versioning and automated release pipelines

### ✅ Conventional Commit Format

---

```bash
<type>[optional scope]: <short description>
[optional body]
[optional footer(s)]
# Example:
feat(api): add endpoint to fetch user transactions
```

---

## 🔖 Commit Types

| Type | Purpose |
| --- | --- |
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation changes only |
| `style` | Code style changes (formatting, white-space, etc., no logic impact) |
| `refactor` | Code changes that neither fix a bug nor add a feature |
| `perf` | Performance improvements |
| `test` | Adding or updating tests |
| `build` | Build system or external dependencies (npm, pip, Docker, etc.) |
| `ci` | CI configuration changes (GitHub Actions, CircleCI, etc.) |
| `chore` | Routine tasks that don't change app behavior (e.g., version bumping) |
| `revert` | Revert a previous commit |

---

## 🧱 Scopes (Optional but Recommended)

Scopes describe the part of the codebase affected. Use folders, layers, or modules as scopes.

Examples:

```bash
feat(api): ...
fix(auth): ...
refactor(etl): ...

```

---

## 🧱 Structuring Project Structure Changes

Use `chore:` or `refactor:` with meaningful scopes when reorganizing files or folders.

### Examples:

```bash
chore(structure): reorganize modules into domain-based folders
chore(files): move shared utils to /lib directory
refactor(project): split monolithic service into microservices
chore(config): extract env config into separate module

```

If the change is **breaking**, include:

```bash
BREAKING CHANGE: import paths have changed for utils and services

```

---

## 🧪 Best Practices

- Use **imperative mood** ("add" not "added")
- Limit summary to **72 characters**
- Use body to explain **why**, not just what
- Use **issue references** in footers:
    
    ```bash
    Closes #101
    
    ```
    
- Use `BREAKING CHANGE:` if the update requires attention

---

## 🛠 Recommended Tools

| Tool | Purpose |
| --- | --- |
| [Commitizen](https://github.com/commitizen/cz-cli) | Interactive commit CLI |
| [Commitlint](https://github.com/conventional-changelog/commitlint) | Lint commit messages |
| [Semantic Release](https://semantic-release.gitbook.io/semantic-release/) | Auto release/changelog |
| [Husky](https://typicode.github.io/husky/#/) | Git hooks for commit-msg validation |

---

## 📜 Git Commit Message & Project Structure Guide

### ✅ Conventional Commit Format

```bash
<type>[optional scope]: <short description>
[optional body]
[optional footer]
```

**Example:**

```bash
feat(api): add endpoint for transaction fetch
```

### 🔖 Commit Types

| Type     | Description                     |
| -------- | ------------------------------- |
| feat     | A new feature                   |
| fix      | A bug fix                       |
| docs     | Docs only changes               |
| style    | Formatting only, no code logic  |
| refactor | Code refactoring                |
| perf     | Performance improvements        |
| test     | Adding or fixing tests          |
| build    | Build tools or dependencies     |
| ci       | CI config files and scripts     |
| chore    | Other changes like tool updates |
| revert   | Reverts previous commits        |

### 🛠 Examples

```bash
feat(auth): implement login with JWT
docs(readme): update installation guide
refactor(services): extract user module
```

### ⚠️ Breaking Changes

```bash
BREAKING CHANGE: auth header format has changed
```

---

## 🔐 SSH Setup (Optional but Recommended)

```bash
ssh-keygen -t rsa -b 4096 -C "you@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub
```

Then add the public key (`id_rsa.pub`) to GitHub > Settings > SSH Keys.

---

## 📚 References

* [Git Book](https://git-scm.com/book/en/v2)
* [Conventional Commits](https://www.conventionalcommits.org/)
* [Semantic Release](https://semantic-release.gitbook.io/semantic-release/)
* [Commitlint](https://commitlint.js.org/)
* [Commitizen](https://github.com/commitizen/cz-cli)
