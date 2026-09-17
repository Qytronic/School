# 💻 School Informatics – Task Solutions

<p align="center">
  <strong>🚀 My Informatics Journey — Python, Jupyter, Git & more</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/VS%20Code-Development-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="VS Code">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/Qytronic/School?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/last-commit/Qytronic/School?style=flat-square" alt="Last Commit">
  <img src="https://img.shields.io/github/repo-size/Qytronic/School?style=flat-square" alt="Repository Size">
</p>

---

## 🚀 About This Repository

Welcome to my **School Informatics** repository.

This repository contains my solutions, exercises, experiments and projects from informatics class.

The main focus is **Python programming**, including:

- 🐍 Regular Python programs
- 📓 Jupyter Notebooks
- ➕ Calculations with Python
- 🎨 Drawing and graphical exercises
- 🧩 Functions
- ⚙️ Functions with parameters
- 🌿 Git branches and version control
- 💻 Visual Studio Code

Instead of storing every topic inside one huge folder, different informatics topics are organized into separate **Git branches**.

> [!NOTE]
> This repository also documents my learning progress.
>  
> Some older solutions may therefore be simpler than newer ones — that's part of the journey.

---

## 📋 Table of Contents

- [🌿 Branches](#-branches)
- [🧠 Topics](#-topics)
- [📖 Project Overview](#-project-overview)
- [📂 File Types](#-file-types)
- [🛠️ Development Setup](#️-development-setup)
- [🧩 VS Code Extensions](#-vs-code-extensions)
- [⚙️ VS Code Configuration](#️-vs-code-configuration)
- [🚀 Getting Started](#-getting-started)
- [🌿 Git Workflow](#-git-workflow)
- [📁 Repository Structure](#-repository-structure)
- [🚫 .gitignore](#-gitignore)
- [🎯 Goals](#-goals)
- [⚖️ Disclaimer](#️-disclaimer)
- [📄 License](#-license)

---

# 🌿 Branches

Different informatics topics are organized into separate **Git branches**.

| Branch | Topic | Description |
|---|---|---|
| [`main`](../../tree/main) | 🏠 Main | Repository documentation, configuration and general files |
| [`Rechnen-mit-Python`](../../tree/Rechnen-mit-Python) | ➕ Rechnen mit Python | Basic calculations, operators, variables and mathematical expressions |
| [`Farben-und-Strichdicke`](../../tree/Farben-und-Strichdicke) | 🎨 Farben & Strichdicke | Drawing exercises with colors and different line widths |
| [`Funktion`](../../tree/Funktion) | 🧩 Funktionen | Creating, calling and reusing Python functions |
| [`Funktionen-mit-Parametern`](../../tree/Funktionen-mit-Parametern) | ⚙️ Funktionen mit Parametern | Passing information into functions using parameters |
| `...` | 🚧 More Topics | Additional topics will be added during the course |

---

## 🔀 Switching Branches

### On GitHub

Use the **branch selector** above the repository file list and choose the topic you want to view.

### Using Git

Fetch all available branches:

```bash
git fetch --all
```

Show all branches:

```bash
git branch -a
```

Switch to a topic:

```bash
git switch Rechnen-mit-Python
```

```bash
git switch Farben-und-Strichdicke
```

```bash
git switch Funktion
```

```bash
git switch Funktionen-mit-Parametern
```

Return to the main branch:

```bash
git switch main
```

---

# 🧠 Topics

## ➕ Rechnen mit Python

The `Rechnen-mit-Python` branch contains exercises about using Python for calculations.

Python can directly be used like a calculator:

```python
5 + 3
10 - 4
6 * 7
20 / 4
2 ** 8
17 % 5
```

### Important Operators

| Operator | Meaning | Example |
|:---:|---|---|
| `+` | Addition | `5 + 3` |
| `-` | Subtraction | `10 - 4` |
| `*` | Multiplication | `6 * 7` |
| `/` | Division | `20 / 4` |
| `//` | Integer Division | `10 // 3` |
| `%` | Modulo / Remainder | `10 % 3` |
| `**` | Power | `2 ** 8` |

### Variables

Values can be stored inside variables:

```python
a = 10
b = 5

result = a * b + 2

print(result)
```

Output:

```text
52
```

Topics include:

- Arithmetic operations
- Variables
- Mathematical expressions
- Operator precedence
- Basic input and output
- Python syntax

---

## 🎨 Farben und Strichdicke

The `Farben-und-Strichdicke` branch contains drawing and graphics exercises.

Topics include:

- Colors
- Line thickness
- Drawing commands
- Coordinates
- Combining multiple commands
- Understanding execution order
- Creating graphical patterns

These exercises help demonstrate how individual instructions can be combined into larger programs.

---

## 🧩 Funktionen

Functions allow code to be grouped into reusable blocks.

Without a function:

```python
print("Hello!")
print("Hello!")
print("Hello!")
```

With a function:

```python
def greeting():
    print("Hello!")
```

The function can now be reused:

```python
greeting()
greeting()
greeting()
```

### Why Functions?

Functions make programs:

- 🧹 Cleaner
- ♻️ Reusable
- 📖 Easier to read
- 🛠️ Easier to modify
- 🧠 Easier to understand

### Basic Structure

```python
def my_function():
    print("This code belongs to the function.")
```

Call the function:

```python
my_function()
```

---

## ⚙️ Funktionen mit Parametern

Parameters make functions more flexible.

Instead of creating a function that always does the same thing:

```python
def greeting():
    print("Hello!")
```

we can pass information into it:

```python
def greeting(name):
    print("Hello", name)
```

The same function can now work with different values:

```python
greeting("Anna")
greeting("Max")
greeting("Alex")
```

Output:

```text
Hello Anna
Hello Max
Hello Alex
```

### Multiple Parameters

Functions can receive multiple values:

```python
def add(a, b):
    print(a + b)
```

Example:

```python
add(5, 3)
```

Output:

```text
8
```

### Returning Values

Functions can also return results:

```python
def multiply(a, b):
    return a * b
```

The returned value can be stored:

```python
result = multiply(6, 7)

print(result)
```

Output:

```text
42
```

### Function Structure

```python
def calculate(a, b):
    result = a + b
    return result
```

```text
def calculate(a, b):
│   │         │
│   │         └── Parameters
│   │
│   └──────────── Function name
│
└──────────────── Function definition
```

---

# 📖 Project Overview

| Category | Details |
|---|---|
| **Language** | Python 3 |
| **IDE** | Visual Studio Code |
| **Notebooks** | Jupyter |
| **Version Control** | Git |
| **Hosting** | GitHub |
| **Linting / Formatting** | Ruff |
| **License** | MIT |

---

# 📂 File Types

## 🐍 `.py`

Regular Python source files.

Example:

```text
exercise.py
```

These files are used for:

- Programming exercises
- Algorithms
- Functions
- Small programs
- Larger projects

Run a Python file with:

```bash
python exercise.py
```

---

## 📓 `.ipynb`

Jupyter Notebook files.

Example:

```text
exercise.ipynb
```

Jupyter Notebooks allow Python code to be split into individual cells and executed interactively.

They are useful for:

- 🧪 Testing code step-by-step
- 📚 School exercises
- 🧠 Learning new concepts
- 📊 Displaying results
- ✍️ Combining explanations and code
- 🔬 Experiments

---

# 🛠️ Development Setup

My main development environment is **Visual Studio Code**.

The setup is focused on:

```text
🐍 Python Development
        +
📓 Jupyter Notebooks
        +
🐞 Debugging
        +
🔍 Linting
        +
🌿 Git
        +
⚡ Productivity
        =
💻 Development Environment
```

---

## 🐍 Python

The Python setup includes:

- **Python** – Core Python support in VS Code
- **Pylance** – IntelliSense, autocomplete and language features
- **Python Debugger** – Debugging with breakpoints and step-by-step execution
- **Python Environments** – Managing Python interpreters and environments
- **Python Indent** – Automatic Python indentation
- **autoDocstring** – Generating Python docstrings
- **Ruff** – Python linting and formatting
- **AREPL for Python** – Fast real-time Python testing

---

## 📓 Jupyter

I use Jupyter for `.ipynb` files.

Extensions:

- **Jupyter** – Notebook support
- **Jupyter Cell Tags** – Cell tagging
- **Jupyter Keymaps** – Jupyter keyboard shortcuts
- **Jupyter Notebook Renderers** – Improved notebook output rendering
- **Jupyter Slideshow** – Using notebooks as presentations

---

## ⚡ Productivity & Code Execution

- **Code Runner** – Quickly run code
- **Error Lens** – Display errors and warnings directly in the editor
- **Indent-Rainbow** – Visualize indentation levels
- **Path Intellisense** – Autocomplete file paths
- **Todo Tree** – Find and organize `TODO` and `FIXME` comments

---

## 🐙 Git

- **GitLens** – Git history, blame information and file history
- **Git Graph** – Visual Git branch and commit history

---

# 🧩 VS Code Extensions

## 🐍 Python

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

## 📓 Jupyter

```text
Jupyter
Jupyter Cell Tags
Jupyter Keymaps
Jupyter Notebook Renderers
Jupyter Slideshow
```

## ⚡ Productivity

```text
Code Runner
Error Lens
Indent-Rainbow
Path Intellisense
Todo Tree
```

## 🌿 Git

```text
GitLens
Git Graph
```

---

# ⚙️ VS Code Configuration

The repository can contain workspace-specific VS Code configuration inside:

```text
.vscode/
├── extensions.json
└── settings.json
```

---

## 💾 Auto Save

I use automatic saving when switching away from the VS Code window.

`.vscode/settings.json`:

```json
{
    "files.autoSave": "onWindowChange"
}
```

---

## 🧩 Recommended Extensions

The repository can recommend useful extensions through:

```text
.vscode/extensions.json
```

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

> [!IMPORTANT]
> These extensions are **recommendations only**.
>
> VS Code does not automatically install them.

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Qytronic/School.git
```

Enter the repository:

```bash
cd School
```

---

## 2️⃣ Open It in VS Code

```bash
code .
```

---

## 3️⃣ Fetch All Branches

```bash
git fetch --all
```

---

## 4️⃣ View Available Branches

```bash
git branch -a
```

Example:

```text
* main
  remotes/origin/Farben-und-Strichdicke
  remotes/origin/Funktion
  remotes/origin/Funktionen-mit-Parametern
  remotes/origin/Rechnen-mit-Python
```

---

## 5️⃣ Switch to a Topic

Example:

```bash
git switch Rechnen-mit-Python
```

or:

```bash
git switch Funktion
```

or:

```bash
git switch Funktionen-mit-Parametern
```

---

# 🌿 Git Workflow

My basic workflow is:

```text
        ┌───────────────┐
        │  Write Code   │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │     Test      │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │ Fix / Improve │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │    git add    │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │  git commit   │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │   git push    │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │    GitHub     │
        └───────────────┘
```

---

## 🔍 Check Status

```bash
git status
```

---

## ➕ Add Changes

Add everything:

```bash
git add .
```

Add a specific file:

```bash
git add exercise.py
```

---

## 💾 Commit Changes

```bash
git commit -m "Add new exercises"
```

---

## ⬆️ Push Changes

```bash
git push
```

---

## 🌱 Create a New Topic Branch

Create and switch to the branch:

```bash
git switch -c new-topic
```

Add changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Add new topic"
```

Push the new branch:

```bash
git push -u origin new-topic
```

---

## 📝 Commit Style

I try to keep commit messages short and descriptive.

### Good Examples

```text
Add calculation exercises
Add function exercises
Add parameter examples
Update README
Fix Python exercise
Improve notebook
Remove unused files
Refactor code
Update VS Code configuration
```

### Bad Examples

```text
stuff
update
changes
idk
test
final
final2
final-final
```

A commit message should make it clear what changed without having to inspect the complete commit.

---

# 📁 Repository Structure

The `main` branch mainly contains documentation and configuration:

```text
School/
│
├── .vscode/
│   ├── extensions.json
│   └── settings.json
│
├── .gitignore
├── LICENSE
└── README.md
```

The exercises themselves are separated into branches:

```text
School Repository
│
├── main
│   └── Documentation & Configuration
│
├── Rechnen-mit-Python
│   └── Python Calculations
│
├── Farben-und-Strichdicke
│   └── Graphics & Drawing
│
├── Funktion
│   └── Python Functions
│
├── Funktionen-mit-Parametern
│   └── Functions with Parameters
│
└── ...
    └── Future Topics
```

This keeps topics separated while preserving everything inside a single repository.

---

# 🚫 `.gitignore`

The repository uses `.gitignore` to prevent unnecessary files from being committed.

Example:

```gitignore
# =========================================================
# Python
# =========================================================

__pycache__/
*.py[cod]
*$py.class


# =========================================================
# Jupyter
# =========================================================

.ipynb_checkpoints/


# =========================================================
# Virtual Environments
# =========================================================

.venv/
venv/
env/


# =========================================================
# Environment Variables
# =========================================================

.env
.env.*


# =========================================================
# Cache
# =========================================================

.cache/
.pytest_cache/
.ruff_cache/


# =========================================================
# Operating System
# =========================================================

.DS_Store
Thumbs.db
desktop.ini


# =========================================================
# Temporary Files
# =========================================================

*.tmp
*.temp
*.log
```

---

# 📈 Learning Progress

The repository grows together with the topics covered in class.

```text
Python Basics
     │
     ▼
Calculations
     │
     ▼
Variables
     │
     ▼
Drawing & Commands
     │
     ▼
Functions
     │
     ▼
Functions with Parameters
     │
     ▼
Reusable Programs
     │
     ▼
More coming...
```

---

# 🎯 Goals

This repository is not only meant to store finished solutions.

It is also used to document:

- 📈 My programming progress
- 🧠 Concepts learned in class
- 🧪 Experiments
- ❌ Mistakes and improvements
- 🛠️ Development tools
- 🌿 Git knowledge
- 🐍 Python skills
- 📓 Jupyter exercises

---

# 🏆 Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Main programming language |
| 📓 **Jupyter** | Interactive notebooks |
| 💻 **Visual Studio Code** | Development environment |
| 🌿 **Git** | Version control |
| 🐙 **GitHub** | Repository hosting |
| ⚡ **Ruff** | Python linting and formatting |
| 🔍 **Pylance** | Python language support |
| 🐞 **Python Debugger** | Debugging |

---

# ⚖️ Disclaimer

This repository contains school work created for:

- Learning
- Practice
- Documentation
- Programming exercises
- Educational purposes

The solutions represent my own work and learning progress.

Other students may inspect the code to:

- Understand programming concepts
- Compare different approaches
- Learn from examples
- Explore Python code

> [!WARNING]
> The solutions should **not be copied and submitted as someone else's own school work**.

Learning programming means understanding **why the code works**, not simply copying code that already works.

Because this repository documents my learning progress, some older solutions may use simpler or less efficient approaches than newer ones.

The code is provided **"as is"** without any guarantee that every solution is error-free or works in every environment.

---

# 📄 License

This project is licensed under the **MIT License**.

See [`LICENSE`](./LICENSE) for the complete license and usage terms.

---

# 🔥 Repository Philosophy

```text
Don't just make it work.

Understand why it works.
Improve it.
Commit it.
Push it.
Learn from it.
```

---

# 📌 Status

This repository is continuously updated as new informatics topics and assignments are completed.

The following may change over time:

- 🌿 Available branches
- 🐍 Python exercises
- 📓 Jupyter Notebooks
- 🧩 VS Code extensions
- ⚙️ Development configuration
- 📁 Repository structure
- 📖 Documentation

---

<p align="center">
  <br>
  <strong>💻 SCHOOL INFORMATICS</strong>
  <br><br>
  <code>Python</code>
  ·
  <code>Jupyter</code>
  ·
  <code>VS Code</code>
  ·
  <code>Git</code>
  ·
  <code>GitHub</code>
  <br><br>
  <strong>Learn. Code. Debug. Commit. Repeat.</strong>
  <br><br>
  🚀
</p>
