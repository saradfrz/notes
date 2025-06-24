# install-pkg.ps1

A PowerShell script to automate Python package installation, dependency management, and Git commit.

## 📦 What It Does

This script simplifies your development workflow:

1. Installs a Python package using `pip install <package>`
2. Updates `requirements.txt` using `pip freeze`
3. Stages `requirements.txt` with Git
4. Commits the changes with a descriptive message: `add: <package>`

## ✅ Requirements

- PowerShell 5.1+ or PowerShell Core (7+)
- Python and `pip` installed and added to PATH
- Git installed and configured
- A Git repository initialized in your project folder

## 🚀 Usage

```powershell
.\install-pkg.ps1 -PackageName <your-package-name>
