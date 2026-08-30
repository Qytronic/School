# 💻 School Informatics – Task Solutions

Welcome to my **School Informatics** repository.

This repository contains my solutions, exercises and projects created during my informatics classes. The main focus of this repository is **Python programming**, including regular Python scripts and Jupyter Notebooks.

I use **Visual Studio Code** as my main development environment.

---

## 📋 Table of Contents

* [📂 Branches](#-branches)

  * [Available Branches](#available-branches)
  * [How to Switch Branches](#how-to-switch-branches)
* [📖 Project Overview](#-project-overview)
* [🛠️ Development Setup](#️-development-setup)

  * [Python](#python)
  * [Jupyter](#jupyter)
  * [Code Quality & Formatting](#code-quality--formatting)
  * [Code Execution](#code-execution)
  * [Productivity & Editor Tools](#productivity--editor-tools)
  * [Git & Version Control](#git--version-control)
* [🧩 VS Code Extensions](#-vs-code-extensions)
* [⚙️ VS Code Configuration](#️-vs-code-configuration)

  * [Auto Save](#auto-save)
  * [Recommended Extensions](#recommended-extensions)
* [🐍 Python & Jupyter Files](#-python--jupyter-files)
* [🌿 Git Workflow](#-git-workflow)
* [📁 Repository Structure](#-repository-structure)
* [⚖️ Legal & Academic Disclaimer](#️-legal--academic-disclaimer)
* [📄 License](#-license)

---

# 📂 Branches

The repository is organized using **Git branches**.

Each branch can contain solutions for a specific topic, task or project. This keeps different topics separated and makes the repository easier to navigate.

## Available Branches

| Branch                                                        | Description                                                                                  |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| [`main`](../../tree/main)                                     | Main branch containing the README, repository configuration and general project information. |
| [`Farben-und-Strichdicke`](../../tree/Farben-und-Strichdicke) | Exercises dealing with colors, line thickness and Python drawing/graphics.                   |
| `...`                                                         | More branches will be added as new topics are covered.                                       |

> **Note:** This list will be updated whenever a new topic branch is created.

---

## How to Switch Branches

### On GitHub

1. Open this repository on GitHub.
2. At the top of the file list, click the **branch selector**.
3. Select the branch you want to view.
4. GitHub will display the files from that branch.

For example, you can switch from:

```text
main
```

to:

```text
Farben-und-Strichdicke
```

### Using Git in the Terminal

First, update the information about remote branches:

```bash
git fetch --all
```

To switch to a specific branch:

```bash
git checkout Farben-und-Strichdicke
```

Or using the newer Git command:

```bash
git switch Farben-und-Strichdicke
```

To see all local and remote branches:

```bash
git branch -a
```

---

# 📖 Project Overview

This repository is used to collect my work from **School Informatics**.

The main purpose is to keep my solutions organized and to document my progress while learning programming.

## Main Technologies

| Technology             | Usage                                        |
| ---------------------- | -------------------------------------------- |
| **Python 3**           | Main programming language                    |
| **Jupyter Notebook**   | Interactive Python exercises and experiments |
| **Git**                | Version control                              |
| **GitHub**             | Remote repository and project hosting        |
| **Visual Studio Code** | Development environment                      |

## File Types

### `.py`

Regular Python source files.

These are mainly used for programming exercises, algorithms and smaller programs.

Example:

```python
print("Hello, World!")
```

### `.ipynb`

Jupyter Notebook files.

Jupyter Notebooks allow code to be divided into individual cells and executed interactively.

They are useful for experimenting with code, documenting solutions and displaying results directly below the corresponding code.

---

# 🛠️ Development Setup

My main development environment is **Visual Studio Code**.

I use several extensions and built-in VS Code features to make writing, testing, debugging and managing Python code easier.

The following sections explain the different parts of my development setup.

---

## Python

Python is the main programming language used in this repository.

### Python

The official **Python** extension provides the basic Python functionality in Visual Studio Code.

It provides features such as:

* Python syntax highlighting
* Running Python files
* Selecting Python interpreters
* Code navigation
* Debugging integration
* Environment support

### Pylance

**Pylance** provides advanced Python language features.

I use it for:

* Autocompletion
* IntelliSense
* Type information
* Error detection
* Code navigation
* Import suggestions

### Python Debugger

The **Python Debugger** allows Python programs to be debugged directly inside VS Code.

It allows me to use:

* Breakpoints
* Step-by-step execution
* Variable inspection
* Call stack inspection
* Debugging controls

This is especially useful when a program does not behave as expected.

### Python Environments

**Python Environments** helps manage and select the Python interpreter used by VS Code.

This is useful when multiple Python versions or virtual environments are available.

### Python Indent

**Python Indent** helps with automatic indentation while writing Python code.

Since indentation is an important part of Python syntax, this makes nested code easier to write and read.

---

# 📓 Jupyter

I also use **Jupyter Notebooks** for `.ipynb` files.

The Jupyter extensions allow notebooks to be opened, edited and executed directly inside Visual Studio Code.

## Jupyter

The **Jupyter** extension provides the main notebook functionality.

It allows me to:

* Open `.ipynb` files
* Create notebook cells
* Run individual cells
* View outputs
* Restart kernels
* Work interactively with Python

## Jupyter Cell Tags

**Jupyter Cell Tags** allows cells to be assigned tags.

Tags can be useful for organizing notebook cells and controlling how certain cells are handled.

## Jupyter Keymaps

**Jupyter Keymaps** provides Jupyter-style keyboard shortcuts inside VS Code.

This makes working with notebooks more convenient.

## Jupyter Notebook Renderers

**Jupyter Notebook Renderers** improves how different notebook outputs are displayed.

This is useful for things such as:

* Tables
* Images
* Plots
* Rich output
* Generated notebook content

## Jupyter Slideshow

**Jupyter Slideshow** allows Jupyter Notebooks to be used as presentations.

Notebook cells can be organized into slides and presented directly from the notebook environment.

---

# 🧹 Code Quality & Formatting

Keeping code readable and detecting problems early is an important part of my development setup.

## Ruff

**Ruff** is used for Python linting and formatting.

It can detect problems in Python code and helps keep the code clean and consistent.

## autoDocstring

**autoDocstring** helps generate documentation strings for Python functions and classes.

For example:

```python
def calculate_area(width, height):
    """
    Calculate the area of a rectangle.

    Args:
        width: Width of the rectangle.
        height: Height of the rectangle.

    Returns:
        The calculated area.
    """
```

This makes functions easier to understand and document.

## Error Lens

**Error Lens** displays errors, warnings and diagnostics directly inside the editor.

Instead of having to look at a separate panel, problems are displayed close to the relevant line of code.

---

# ▶️ Code Execution

## AREPL for Python

**AREPL for Python** provides a real-time environment for testing Python code.

It is useful for quickly experimenting with small pieces of Python without having to manually run the complete program every time.

## Code Runner

**Code Runner** provides a quick way to execute code directly from Visual Studio Code.

It can be used to quickly run Python files or selected pieces of code.

---

# 🎨 Productivity & Editor Tools

## Indent-Rainbow

**Indent-Rainbow** visually highlights different indentation levels.

This makes deeply nested Python code easier to read.

Example:

```python
if condition:
    for item in items:
        if item > 10:
            print(item)
```

The different indentation levels become easier to distinguish visually.

## Path Intellisense

**Path Intellisense** provides autocomplete for file and directory paths.

This is useful when working with:

* File paths
* Imports
* Directories
* Project files

## Todo Tree

**Todo Tree** searches the project for comments such as:

```python
# TODO: Finish this function
# FIXME: Fix this problem
```

These tasks can then be displayed in a dedicated sidebar view.

---

# 🐙 Git & Version Control

Git is used to track changes in this repository.

I use **GitLens** and **Git Graph** to make Git easier to understand and manage inside Visual Studio Code.

## GitLens

**GitLens** provides additional Git information directly inside VS Code.

For example, it can show:

* Who changed a line
* When a line was changed
* Commit history
* File history
* Branch information
* Code authorship information

## Git Graph

**Git Graph** provides a visual representation of Git history.

It allows branches, commits and merges to be viewed as a graph.

This makes it easier to understand how the different branches of the repository are connected.

---

# 🧩 VS Code Extensions

The following is the current list of VS Code extensions used for this project.

## 🐍 Python

* **Python**
* **Pylance**
* **Python Debugger**
* **Python Environments**
* **Python Indent**
* **autoDocstring**
* **Ruff**
* **AREPL for Python**

## 📓 Jupyter

* **Jupyter**
* **Jupyter Cell Tags**
* **Jupyter Keymaps**
* **Jupyter Notebook Renderers**
* **Jupyter Slideshow**

## ⚡ Development & Productivity

* **Code Runner**
* **Error Lens**
* **Path Intellisense**
* **Indent-Rainbow**
* **Todo Tree**

## 🐙 Git

* **GitLens**
* **Git Graph**

> The extension list may change over time as my development environment evolves.

---

# ⚙️ VS Code Configuration

In addition to extensions, I use several built-in Visual Studio Code settings.

## Auto Save

I use VS Code's automatic saving feature.

The setting is configured as:

```json
{
    "files.autoSave": "onWindowChange"
}
```

This means that modified files are automatically saved when switching away from the VS Code window.

This helps prevent accidentally leaving changes unsaved.

---

## Recommended Extensions

The repository can contain a `.vscode` folder with an `extensions.json` file:

```text
.vscode/
└── extensions.json
```

The file can contain the extensions recommended for this repository.

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

When the repository is opened in Visual Studio Code, VS Code can offer to install the recommended extensions.

---

# 🐍 Python & Jupyter Files

This repository mainly contains two types of source files.

## Python Scripts

Python scripts use the `.py` file extension.

They are used for regular programming exercises and applications.

Example:

```text
exercise.py
solution.py
main.py
```

## Jupyter Notebooks

Jupyter Notebooks use the `.ipynb` file extension.

They are used when working interactively with Python code.

Example:

```text
exercise.ipynb
analysis.ipynb
```

A notebook can contain:

* Python code
* Text explanations
* Output
* Tables
* Images
* Graphs

---

# 🌿 Git Workflow

My general workflow for working on this repository looks like this:

```text
Write Code
    ↓
Test Code
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

## 1. Check the Current Status

Before committing changes, I can check the current repository status:

```bash
git status
```

This shows which files have been modified, added or deleted.

## 2. Add Changes

To stage all changes:

```bash
git add .
```

## 3. Create a Commit

A commit saves a snapshot of the current changes:

```bash
git commit -m "Add new informatics exercises"
```

A commit message should briefly describe what was changed.

## 4. Push Changes

To upload the commit to GitHub:

```bash
git push
```

---

# 🌱 Working With Branches

Branches are used to keep different topics separated.

For example, a new topic can be created with:

```bash
git switch -c new-topic
```

After working on the branch:

```bash
git add .
git commit -m "Add new topic exercises"
git push -u origin new-topic
```

The new branch can then be viewed separately on GitHub.

---

# 📁 Repository Structure

The general structure of the repository is:

```text
School-Informatics/
│
├── README.md
├── LICENSE
├── .gitignore
│
└── .vscode/
    └── extensions.json
```

The actual programming files are organized inside the corresponding topic branches.

For example:

```text
Farben-und-Strichdicke/
│
├── exercise_01.py
├── exercise_02.py
└── ...
```

More branches and files will be added as new informatics topics are covered.

---

# 🚫 Files That Should Not Be Uploaded

Some temporary or automatically generated files should generally not be committed to Git.

For example:

```text
__pycache__/
*.py[cod]
.ipynb_checkpoints/
```

A `.gitignore` file can be used to tell Git which files should be ignored.

Example:

```gitignore
__pycache__/
*.py[cod]
.ipynb_checkpoints/
```

Depending on the project, additional files or folders may also be added to `.gitignore`.

---

# ⚖️ Legal & Academic Disclaimer

This repository contains solutions and work created as part of school informatics education.

The repository is primarily intended for **personal documentation, learning and portfolio purposes**.

## Academic Integrity

The solutions represent my own work and learning progress.

Other students may inspect the repository to understand programming concepts or different approaches. However, the code should **not be copied and submitted as someone else's work** for school assignments.

If a specific assignment or school has additional rules regarding the use of solutions, those rules take precedence.

## No Warranty

The code in this repository is provided **"as is"**.

I make no guarantee that every program is completely free of errors or that the code will work in every environment.

Use the code at your own risk.

## Copyright

Unless explicitly stated otherwise, the original code and documentation in this repository are protected by applicable copyright law.

The permissions for using, copying, modifying or redistributing the code are defined by the repository's `LICENSE` file.

---

# 📄 License

This repository contains a `LICENSE` file.

Please read the license before using, modifying or redistributing code from this repository.

---

# 📌 Notes

This repository is continuously updated as new topics and assignments are completed.

The branch structure, development tools and VS Code setup may therefore change over time.

**Last updated:** 2026
