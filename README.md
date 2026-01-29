# CS101: Data Structures

Activity 02: Getting Started with UV Package Manager

## Assigned: Friday, 30th January 2026

## Due: END OF CLASS: Friday, 30th January 2026, by 11:00am via GitHub

## Table of contents
- [CS101: Data Structures](#cs101-data-structures)
  - [Assigned: Friday, 30th January 2026](#assigned-friday-30th-january-2026)
  - [Due: END OF CLASS: Friday, 30th January 2026, by 11:00am via GitHub](#due-end-of-class-friday-30th-january-2026-by-1100am-via-github)
  - [Table of contents](#table-of-contents)
  - [Deliverables](#deliverables)
  - [Project Goals](#project-goals)
  - [Introduction to UV Package Manager](#introduction-to-uv-package-manager)
    - [What is UV?](#what-is-uv)
    - [Why Use UV?](#why-use-uv)
  - [Part 1: Installing UV](#part-1-installing-uv)
    - [MacOS Installation](#macos-installation)
    - [Linux/Unix Installation](#linuxunix-installation)
    - [Windows Installation](#windows-installation)
    - [Verifying Your Installation](#verifying-your-installation)
    - [Additional Resources](#additional-resources)
  - [Part 2: Tutorial 1 - Basic Plotting with Data Structures](#part-2-tutorial-1---basic-plotting-with-data-structures)
  - [Part 3: Tutorial 2 - Prime Number Distribution Analysis](#part-3-tutorial-2---prime-number-distribution-analysis)
  - [Reflection Questions](#reflection-questions)
  - [Checking Your Work](#checking-your-work)

## Deliverables

You are to complete and push to your repository the following files:

- `tutorials/tutorial_01_basic_plotting/plotting.py` - Completed Python source code
- `tutorials/tutorial_02_prime_distribution/primes.py` - Completed Python source code
- `writing/reflection.md` - Reflection document with answers to all questions

## Project Goals

- To learn how to install and use UV, a modern Python package manager.
- To understand how package managers help manage project dependencies.
- To practice creating data structures (lists) in Python to visualize data.
- To explore mathematical concepts through data visualization.
- To develop skills in working with isolated virtual environments.

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## Introduction to UV Package Manager

### What is UV?

UV is an extremely fast Python package installer and resolver, written in Rust. It serves as a drop-in replacement for pip and pip-tools, but with significantly improved performance and a better user experience. UV helps you manage Python projects, dependencies, and virtual environments efficiently.

### Why Use UV?

- **Speed**: UV is 10-100x faster than pip for installing packages
- **Reliability**: Better dependency resolution than pip
- **Simplicity**: Easy-to-use interface for creating and managing projects
- **Compatibility**: Works seamlessly with existing Python tools and workflows
- **Isolation**: Creates isolated environments for each project automatically

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## Part 1: Installing UV

For help during any of the following steps, please check the UV website at; [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/).

### MacOS Installation

**Option 1: Using Homebrew (Recommended)**

```bash
brew install uv
```

**Option 2: Using curl**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, you may need to restart your terminal or run:

```bash
source $HOME/.cargo/env
```

### Linux/Unix Installation

**Using curl (All Linux distributions)**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, restart your terminal or run:

```bash
source $HOME/.cargo/env
```

**Alternative: Using pip (if you already have Python)**

```bash
pip install uv
```

### Windows Installation

**Option 1: Using PowerShell (Recommended)**

Open PowerShell and run:

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Option 2: Using pip (if you already have Python)**

```bash
pip install uv
```

**Option 3: Using winget**

```bash
winget install --id=astral-sh.uv -e
```

### Verifying Your Installation

To verify that UV is installed correctly, open a terminal and run:

```bash
uv --version
```

You should see output showing the UV version number (e.g., `uv 0.5.20` or similar).

### Additional Resources

If you encounter any issues during installation or want to learn more about UV:

- **Official UV Documentation**: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)
- **UV GitHub Repository**: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)
- **UV Getting Started Guide**: [https://docs.astral.sh/uv/getting-started/](https://docs.astral.sh/uv/getting-started/)
- **UV Installation Guide**: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)
- **Python Packaging User Guide**: [https://packaging.python.org/](https://packaging.python.org/)

**Troubleshooting Tips**:

- If `uv` command is not found after installation, make sure your PATH environment variable is set correctly
- On Windows, you may need to restart your terminal or computer after installation
- If you have permission issues, avoid using `sudo` with UV; instead, use the curl installation method
- For university/corporate computers with restricted permissions, contact your IT department

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## Part 2: Tutorial 1 - Basic Plotting with Data Structures

In this tutorial, you'll create a UV project that demonstrates data visualization using matplotlib, pandas, and plotly libraries. You will practice creating lists from loops and using them to generate interesting plots.

**Location**: [tutorials/tutorial_01_basic_plotting/](tutorials/tutorial_01_basic_plotting/)

**What you'll do**:

1. Initialize a UV project
2. Complete TODO sections to generate data using `range()` loops
3. Run the provided plotting code to visualize your data
4. Explore different plot types: line plots, bar charts, and scatter plots

**Getting Started**:

```bash
cd tutorials/tutorial_01_basic_plotting
uv init
uv add matplotlib pandas plotly
uv run plotting.py
```

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## Part 3: Tutorial 2 - Prime Number Distribution Analysis

In this tutorial, you'll work with a more complex project that explores prime number distributions. You'll write loops to generate prime numbers and analyze their mathematical properties using visualization.

**Location**: [tutorials/tutorial_02_prime_distribution/](tutorials/tutorial_02_prime_distribution/)

**What you'll do**:

1. Initialize a UV project with required dependencies
2. Complete loops to identify prime numbers
3. Analyze the distribution of primes using ln(n) relationships
4. Investigate twin prime distributions
5. Visualize mathematical patterns in prime numbers

**Getting Started**:

```bash
cd tutorials/tutorial_02_prime_distribution
uv init
uv add matplotlib pandas plotly numpy
uv run primes.py
```

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## Reflection Questions

After completing both tutorials, answer the reflection questions in the `writing/reflection.md` file. These questions will help you think about package managers, virtual environments, and the code you wrote.

![--- --- --- --- --- --- --- --- ---](graphics/div_bar.png)

## Checking Your Work

To check if your work meets the assignment requirements, you can use GatorGrade:

```bash
gatorgrade --config config/gatorgrade.yml
```

This will automatically verify:

- All required files exist
- All TODO markers have been removed
- The reflection document is complete
- You have made at least 5 commits to your repository

**Note**: Make sure to commit your changes regularly throughout the activity using:

```bash
git add .
git commit -m "Descriptive message about your changes"
git push
```

Good luck, and enjoy exploring Python package management with UV!
