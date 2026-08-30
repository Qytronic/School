# 💻 School Informatics – Task Solutions

Welcome to my **School Informatics** repository.

This repository contains my solutions, exercises and projects from informatics class. The main focus is **Python programming**, including regular Python files and Jupyter Notebooks.

I use **Visual Studio Code** as my main development environment and **Git/GitHub** for version control.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/VS%20Code-Development-blue?logo=visualstudiocode&logoColor=white" alt="VS Code">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/Git-Version%20Control-F05032?logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/github/license/Qytronic/School" alt="License">
</p>

---

## 📋 Table of Contents

- [📂 Branches](#-branches)
- [📖 Project Overview](#-project-overview)
- [🛠️ Development Setup](#️-development-setup)
- [🧩 VS Code Extensions](#-vs-code-extensions)
- [⚙️ VS Code Configuration](#️-vs-code-configuration)
- [🌿 Git Workflow](#-git-workflow)
- [📁 Repository Structure](#-repository-structure)
- [🚫 .gitignore](#-gitignore)
- [⚖️ Disclaimer](#️-disclaimer)
- [📄 License](#-license)

---

## 📂 Branches

Different informatics topics are organized into separate **Git branches**.

| Branch | Description |
|---|---|
| [`main`](../../tree/main) | Main repository, documentation and configuration |
| [`Farben-und-Strichdicke`](../../tree/Farben-und-Strichdicke) | Colors, line thickness and drawing exercises |
| `...` | More topics will be added |

### How to switch branches

On GitHub, use the **branch selector** above the file list and choose the branch you want to view.

Using the terminal:

```bash
git fetch --all
git switch Farben-und-Strichdicke
```

To see all branches:

```bash
git branch -a
```

---

## 📖 Project Overview

| Category | Details |
|---|---|
| **Language** | Python 3 |
| **IDE** | Visual Studio Code |
| **Notebooks** | Jupyter |
| **Version Control** | Git |
| **Hosting** | GitHub |
| **License** | MIT |

### File Types

**`.py`**  
Regular Python source files for programming exercises, algorithms and projects.

**`.ipynb`**  
Jupyter Notebook files for interactive Python development, experiments and documented solutions.

---

## 🛠️ Development Setup

My main development environment is **Visual Studio Code**.

The setup is focused on Python development, Jupyter Notebooks, debugging, code quality, Git and general productivity.

### 🐍 Python

The Python setup includes:

- **Python** – Core Python support in VS Code
- **Pylance** – IntelliSense, autocomplete and language features
- **Python Debugger** – Debugging with breakpoints and step-by-step execution
- **Python Environments** – Managing Python interpreters and environments
- **Python Indent** – Automatic Python indentation
- **autoDocstring** – Generating Python docstrings
- **Ruff** – Python linting and formatting
- **AREPL for Python** – Fast real-time Python testing

### 📓 Jupyter

I use Jupyter for `.ipynb` files.

Extensions:

- **Jupyter** – Notebook support
- **Jupyter Cell Tags** – Cell tagging
- **Jupyter Keymaps** – Jupyter keyboard shortcuts
- **Jupyter Notebook Renderers** – Improved notebook output rendering
- **Jupyter Slideshow** – Using notebooks as presentations

### ⚡ Productivity & Code Execution

- **Code Runner** – Quickly run code
- **Error Lens** – Display errors and warnings directly in the editor
- **Indent-Rainbow** – Visualize indentation levels
- **Path Intellisense** – Autocomplete file paths
- **Todo Tree** – Find and organize `TODO` and `FIXME` comments

### 🐙 Git

- **GitLens** – Git history, blame information and file history
- **Git Graph** – Visual Git branch and commit history

---

## 🧩 VS Code Extensions

### Python

```text
Python
Pylance
Python Debugger
Python Environments
Python Indent
autoDocstring
Ruff
AREPL for Python
```

### Jupyter

```text
Jupyter
Jupyter Cell Tags
Jupyter Keymaps
Jupyter Notebook Renderers
Jupyter Slideshow
```

### Productivity

```text
Code Runner
Error Lens
Indent-Rainbow
Path Intellisense
Todo Tree
```

### Git

```text
GitLens
Git Graph
```

---

## ⚙️ VS Code Configuration

The repository can contain workspace-specific VS Code configuration in:

```text
.vscode/
├── extensions.json
└── settings.json
```

### Auto Save

I use automatic saving when switching away from the VS Code window:

```json
{
    "files.autoSave": "onWindowChange"
}
```

### Recommended Extensions

The repository can recommend extensions through `.vscode/extensions.json`.

Example:

```json
{
    "recommendations": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.debugpy",
        "ms-toolsai.jupyter",
        "charliermarsh.ruff",
        "eamodio.gitlens",
        "mhutchie.git-graph",
        "usernamehw.errorlens",
        "formulahendry.code-runner",
        "gruntfuggly.todo-tree"
    ]
}
```

These are **recommendations**, not forced installations.

---

## 🌿 Git Workflow

My basic workflow is:

```text
Write Code
    ↓
Test
    ↓
Fix / Improve
    ↓
git add
    ↓
git commit
    ↓
git push
    ↓
GitHub
```

### Check Status

```bash
git status
```

### Add Changes

```bash
git add .
```

### Commit Changes

```bash
git commit -m "Add new exercises"
```

### Push Changes

```bash
git push
```

### Create a New Topic Branch

```bash
git switch -c new-topic
git add .
git commit -m "Add new topic"
git push -u origin new-topic
```

### Commit Style

I try to keep commit messages short and descriptive.

Examples:

```text
Add new exercises
Update README
Fix Python exercise
Remove unused files
Refactor code
```

---

## 📁 Repository Structure

The general structure of the main branch is:

```text
School/
├── .vscode/
│   ├── extensions.json
│   └── settings.json
│
├── .gitignore
├── LICENSE
├── README.md
│
└── topic branches
    ├── Farben-und-Strichdicke
    └── ...
```

The actual exercises and projects are stored in their respective topic branches.

---

## 🚫 .gitignore

The repository uses `.gitignore` to prevent temporary or unnecessary files from being committed.

Example:

```gitignore
# Python
__pycache__/
*.py[cod]

# Jupyter
.ipynb_checkpoints/

# Environment files
.env
```

---

## ⚖️ Disclaimer

This repository contains school work created for **learning, documentation and educational purposes**.

The solutions represent my own work and learning progress.

Other students may inspect the code to understand concepts or different approaches, but the solutions should **not be copied and submitted as someone else's school work**.

The code is provided **"as is"** without any guarantee that it is error-free or works in every environment.

---

## 📄 License

This project is licensed under the **MIT License**.

See [`LICENSE`](./LICENSE) for the complete license and usage terms.

---

## 📌 Notes

This repository is continuously updated as new informatics topics and assignments are completed.

The following may change over time:

- Available branches
- Exercises and projects
- VS Code extensions
- Development configuration
- Repository structure

<p align="center">
  <strong>School Informatics · Python · Jupyter · Git · GitHub · VS Code</strong>
</p>
