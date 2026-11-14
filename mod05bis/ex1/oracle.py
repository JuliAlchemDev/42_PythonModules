import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEYS = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL",
        "ZION_ENDPOINT"]
DEFAULTS = {"MATRIX_MODE": "development", "LOG_LEVEL": "INFO"}


def load_env_file() -> bool:
    try:
        from dotenv import load_dotenv
    except ModuleNotFoundError as error:
        print("Missing module:", error)
        print("Hint:")
        print("1. Create a virtual environment:")
        print("   $ python3 -m venv lab_env")
        print("2. Activate it:")
        print("   $ source lab_env/bin/activate")
        print("3. Install the dependencies:")
        print("   $ pip install -r requirements.txt\n")
        return False

    env_path = os.path.join(BASE_DIR, ".env")
    if not os.path.isfile(env_path):
        print("No .env file was found!")
        print("Hint:")
        print("   $ cp .env.example .env\n")
        return False

    load_dotenv(env_path, override=False)
    return True


def read_config() -> tuple[dict[str, str], list[str]]:

    config: dict[str, str] = {}
    warnings: list[str] = []

    for key in KEYS:
        value = os.getenv(key)
        if value:
            config[key] = value
        elif key in DEFAULTS:
            config[key] = DEFAULTS[key]
            warnings.append(f"{key} not set, using default '{DEFAULTS[key]}'")
        else:
            config[key] = ""
            warnings.append(f"{key} not set")

    return config, warnings


def check_security(overrides_ok: bool) -> None:
    print("\nConfiguration security check:")

    try:
        with open(os.path.abspath(__file__), "r") as file:
            source = file.read()
        api_key = os.getenv("API_KEY", "")
        if api_key and api_key in source:
            print("[KO] API_KEY value found in the source code")
        else:
            print("[OK] No hardcoded secrets detected")

    except OSError as error:
        print(f"[KO] {error}")

    try:
        path = os.path.join(BASE_DIR, ".gitignore")
        with open(path, "r") as file:
            lines = [line.strip() for line in file.read().splitlines()]
        if ".env" in lines:
            print("[OK] .env file properly ignored by git")
        else:
            print("[KO] .env is not listed in .gitignore")
    except OSError as error:
        print(f"[KO] {error}")

    if overrides_ok:
        print("[OK] Production overrides available")
    else:
        print("[KO] .env replaced values from the environment")


def main() -> None:
    status = "Consulting the configuration..."
    print(f"\nORACLE STATUS: {status}\n")

    before = {k: os.environ[k] for k in KEYS if k in os.environ}

    if not load_env_file():
        print("Continuing with environment variables and defaults.\n")
    overrides_ok = all(os.environ.get(k) == v for k, v in before.items())

    config, warnings = read_config()

    mode = config["MATRIX_MODE"].lower()
    if mode not in ["development", "production"]:
        warnings.append(f"Unknown MATRIX_MODE '{mode}', using development")
        mode = "development"

    errors: list[str] = []
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    db_url = config["DATABASE_URL"]
    if not db_url:
        db_status = "Not configured"
    elif mode == "development" and "localhost" in db_url:
        db_status = "Connected to local instance"
    else:
        db_status = "Remote instance configured"
    print(f"Database: {db_status}")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: 403 Forbidden")

    print(f"Log Level: {config["LOG_LEVEL"]}")
    print("Remote Network: "
          f"{'Online' if config["ZION_ENDPOINT"] else 'Offline'}"
          )

    if mode == "production":
        for key in ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT"):
            if not config[key]:
                errors.append(f"{key} is required in production")
        if config["LOG_LEVEL"].upper() == "DEBUG":
            warnings.append("DEBUG logging is not recommended in production")
    else:
        if config["DATABASE_URL"]:
            print(f"Database host: {config['DATABASE_URL']}")

    if warnings:
        print()
        for warning in warnings:
            print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    check_security(overrides_ok)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
