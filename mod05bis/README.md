# Python Module 05 — Packages, Environments and the Alchemist’s Toolchain

## Exercises Overview

### Exercise 0: The Sealed Laboratory

#### Part 1: Sealing the Room

Detect whether Python is running inside a virtual environment and display information about the current environment, including its package installation location.

**Concepts**:

- **Virtual environment:** an isolated Python environment created with `venv`.
- **Global environment:** the base Python installation, shared by other projects.
- Detecting a virtual environment by comparing `sys.prefix` and `sys.base_prefix`.
- Getting the path of the active Python interpreter with `sys.executable`.
- Extracting the environment name from a path with `os.path.basename()`.
- Retrieving package installation locations with `site.getsitepackages()`.
- Creating a virtual environment with `python3 -m venv`.
- Activating a virtual environment on Unix (`source`) and Windows (`Scripts\activate`).
- **Package isolation:** packages installed inside a virtual environment do not affect the global environment.

#### Part 2: Stocking the Reagents

Create a dependency loader that checks whether the required external packages (`pandas` and `numpy`) are installed and can be imported, displays their versions, and provides installation instructions when something goes wrong.

**Concepts**:
- Declaring dependencies in `requirements.txt`.
- Installing dependencies with `pip install -r requirements.txt`.
- Using `importlib.import_module()` for dynamic imports.
- Retrieving package versions with `__version__`.
- Handling `ModuleNotFoundError` and `ImportError`.
- Providing installation instructions with pip and Poetry.
- Understanding the difference between an installed package and a package that can be successfully imported.
- Dependency version constraints (`>=`).
- Understanding pip dependency installation and resolution.
