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
- Understanding the difference between an installed package and a successfully imported package.
- Dependency version constraints (`>=`).
- Understanding pip dependency installation and resolution.
- Declaring project dependencies in `pyproject.toml`.
- Managing dependencies and virtual environments with Poetry.
- Understanding the role of `poetry.lock` in reproducible installations.
- Understanding dependency isolation and the difference between pip and Poetry environments.



### Exercise 2: The Alembic

Build a modular Python package and test different import mechanisms to access functions from standalone modules and packages.

**Concepts**:

| **Module** | **Package** |
|---|---|
| A `.py` file containing reusable code (functions, variables, etc.). | A directory grouping related Python modules. |

- `__init__.py`: initializes a package and defines its public interface.
- `import module_name` and `from module_name import function_name`.
- Accessing module attributes using dot notation (`module.function()`).
- **Relative imports:** referencing modules within the current package (`from .elements import create_air`).
- **Package interface:** exposing selected functions through the package namespace.
- Difference between a function defined in a module and one exposed by the package.
- `AttributeError`: accessing an unavailable attribute.


#### Sources
- Absolute and Relative Imports in Python [geeksforgeeks](https://www.geeksforgeeks.org/python/absolute-and-relative-imports-in-python/)


### Exercise 3: Distillation and Transmutation

Build a potion system using nested imports, combining modules from different locations and accessing functions across packages and subpackages.

**Concepts**:

- Importing modules from different locations within a project.
- Absolute imports: referencing modules from the project import path.
- Relative imports: referencing modules from the current package and its parent packages.
- Nested packages and subpackages.
- Using `from ... import ...` to access modules directly.
- Using `import ...` to access nested modules through dot notation.
- Import aliases to distinguish modules with the same name.
- Understanding package context when executing modules.
- Running a package module with `python -m package.module`.
- Combining absolute and relative imports within the same module.

### Exercise 4: Avoid the Explosion

