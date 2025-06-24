# `installpkg.sh`

A simple Bash script to install a Python package, update the `requirements.txt` file, and commit the change to Git for better dependency tracking and version control.

## 📄 Description

This script automates the common Python development workflow of:

1. Installing a new package via `pip`.
2. Updating the `requirements.txt` file with current dependencies.
3. Staging and committing the updated requirements file to a Git repository.

## 🚀 Usage

```bash
./installpkg.sh <package-name>
```

### Example:

```bash
./installpkg.sh requests
```

## 💻 Platform Compatibility

This script is intended to be run in **Unix-like environments** that support **Bash**:

* ✅ Linux terminals
* ✅ macOS Terminal
* ✅ Windows (via [WSL](https://learn.microsoft.com/en-us/windows/wsl/install), [Git Bash](https://gitforwindows.org/), or Cygwin)
* ❌ Not compatible with Windows Command Prompt or PowerShell without a Bash interpreter

To use this script on Windows, install [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) or use [Git Bash](https://gitforwindows.org/).

## 🔧 Requirements

* Python and `pip` installed
* Git initialized in the project directory
* Bash shell environment
* Script execution permission (`chmod +x installpkg.sh`)

## 💡 Notes

* If no package name is supplied, the script will exit with a usage message.
* The script only commits the `requirements.txt` file. Ensure your Git working directory is clean or staged as needed.

## 📁 Example Output

```bash
Installing package: requests
Updating requirements.txt
Staging requirements.txt
Committing changes
[main abc1234] add: requests
Done
```

## 🧼 Best Practices

* Use virtual environments to isolate dependencies.
* Review changes to `requirements.txt` before committing to avoid unwanted upgrades.
