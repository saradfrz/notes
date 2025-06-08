# 🖥️ Custom Linux Bash Prompt with Git Branch and Color Indicators

This script defines a **custom Bash prompt** (`PS1`) for **Linux systems**. It includes color formatting, the current Git branch (if applicable), and success/failure symbols after each command.

---

## ⚠️ Compatibility

> **Works only on Linux** systems using the **Bash** shell.
> Not guaranteed to work on macOS (uses `.bash_profile`) or Windows (unless using WSL).

---

## ✅ Features

* 🎨 **Color-coded** `user@host:path`
* 🌿 Shows **Git branch** in active directory
* ✔️/✖️ Indicates **last command success or failure**
* Multi-line prompt with modern, clear formatting

---

## 🔧 Example Output

```bash
alice@my-machine:~/dev/myproject main
✔ $
```

If the last command failed:

```bash
alice@my-machine:~/dev/myproject main
✖ $
```

---

## 🧱 Code Breakdown

### 🎨 Define Colors

```bash
RED="\[\033[0;31m\]"
GREEN="\[\033[0;32m\]"
YELLOW="\[\033[0;33m\]"
BLUE="\[\033[1;34m\]"
MAGENTA="\[\033[1;35m\]"
CYAN="\[\033[1;36m\]"
WHITE="\[\033[1;37m\]"
RESET="\[\033[0m\]"
```

### 🌿 Git Branch Parser

```bash
parse_git_branch() {
  git rev-parse --abbrev-ref HEAD 2>/dev/null
}
```

### ✅❌ Status Symbols

```bash
PROMPT_SYMBOL_SUCCESS="${GREEN}✔${RESET}"
PROMPT_SYMBOL_ERROR="${RED}✖${RESET}"
```

### 🛠️ Final `PS1` Prompt

```bash
PS1="\${debian_chroot:+(\$debian_chroot)}"\
"${CYAN}\u${WHITE}@${MAGENTA}\h${RESET}:"\
"${BLUE}\w${RESET}"\
"${GREEN} \$(parse_git_branch)${RESET}"\
'\n'\
"\$(if [[ \$? == 0 ]]; then echo \"${PROMPT_SYMBOL_SUCCESS}\"; else echo \"${PROMPT_SYMBOL_ERROR}\"; fi) "\
"${YELLOW}\\$ ${RESET}"
```

---

## 📥 Installation

1. Open your `.bashrc` file:

   ```bash
   nano ~/.bashrc
   ```
2. Paste the full snippet.
3. Apply changes:

   ```bash
   source ~/.bashrc
   ```

---

## 📚 References

* [GNU Bash Prompt Documentation](https://www.gnu.org/software/bash/manual/html_node/Controlling-the-Prompt.html)
* [Git rev-parse Command](https://git-scm.com/docs/git-rev-parse)
* [ANSI Colors in Bash](https://misc.flogisoft.com/bash/tip_colors_and_formatting)
