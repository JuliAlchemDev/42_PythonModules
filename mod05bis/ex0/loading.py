import importlib

REQUIRED_DEPENDENCIES = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation"
}


def show_hint(module: str) -> None:
    print("  # use pip/Poetry the install command")
    print(f"  $ pip install {module}")
    print(f"  $ poetry add {module}")


def main() -> None:
    """
    [TODO]: pyproject.toml  & poetry
    """

    status = "Loading reagents..."
    all_ok = True
    print(f"\nREAGENT STATUS: {status}\n")

    print("Checking dependencies:")

    for dep, desc in REQUIRED_DEPENDENCIES.items():
        try:
            module = importlib.import_module(dep)
            version = module.__version__
            print(f"[OK] {dep} ({version}) - {desc} ready")
        except (ModuleNotFoundError, ImportError) as error:
            all_ok = False
            print(f"[KO] {error}")
            show_hint(dep)

    print()
    print("pip vs Poetry:")
    print(
        "  requirements.txt declares what to install;",
        "pip resolves it at install time.")
    print(
        "  pyproject.toml declares the same constraints,",
        "and Poetry pins the resolved\n",
        " versions in poetry.lock so every install is identical.")

    if (all_ok):
        print()
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
