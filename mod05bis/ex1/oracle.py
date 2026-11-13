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
    print("Configuration loaded:")
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

    # print("Mode:", os.getenv("MATRIX_MODE"))

    # db_url = os.getenv("DATABASE_URL")
    # print("Database: ", end="")
    # if (db_url):
    #     print("Connected to local instance")
    # else:
    #     print("Not configured")

    # api_key = os.getenv("API_KEY")
    # print("API Access: ", end="")
    # if (api_key):
    #     print("Authenticated")
    # else:
    #     print("403 Forbidden")

    # print("Log Level:", os.getenv("LOG_LEVEL", "DEBUG"))

    # endpoint = os.getenv("ZION_ENDPOINT")
    # print("Remote Network: ", end="")
    # if (endpoint):
    #     print("Online")
    # else:
    #     print("Offline")
    # # print(os.environ)  # shows all en variables

# def check_security():
#     print("\nConfiguration security check:")

# # ("[OK] No hardcoded secrets detected")
#     try:
#         with open("./.gitignore", "r") as file:
#             # check .envdfaf case! | file.read().splitlines()
#             has_env = ".env" in file.read()
#             if (has_env):
#                 print("[OK] .env file properly ignored by git")
#             else:
#                 print("[KO] .env is not listed in .gitignore")
#     except OSError as error:
#         print(f"[KO] {error}")
# # ("[OK] Production overrides available")

def main() -> None:
    status = "Consulting the configuration..."
    print(f"\nORACLE STATUS: {status}\n")

    if load_env_file():
        config, warning = read_config()

    # check_security()


if __name__ == "__main__":
    main()
