#  python3 -m venv lab_env
#  source lab_env/bin/activate

# pip install -r requirements.txt
# cp .env.example .env

import os
from dotenv import load_dotenv


def check_security():
    print("\nConfiguration security check:")

# ("[OK] No hardcoded secrets detected")
    try:
        with open("./.gitignore", "r") as file:
            # check .envdfaf case! | file.read().splitlines()
            has_env = ".env" in file.read()
            if (has_env):
                print("[OK] .env file properly ignored by git")
            else:
                print("[KO] .env is not listed in .gitignore")
    except OSError as error:
        print(f"[KO] {error}")


# ("[OK] Production overrides available")


def main() -> None:
    status = "Consulting the configuration..."
    print(f"\nORACLE STATUS: {status}\n")

    load_dotenv()
    print("Mode:", os.getenv("MATRIX_MODE"))

    db_url = os.getenv("DATABASE_URL")
    print("Database: ", end="")
    if (db_url):
        print("Connected to local instance")
    else:
        print("Not configured")

    api_key = os.getenv("API_KEY")
    print("API Access: ", end="")
    if (api_key):
        print("Authenticated")
    else:
        print("403 Forbidden")

    print("Log Level:", os.getenv("LOG_LEVEL", "DEBUG"))

    endpoint = os.getenv("ZION_ENDPOINT")
    print("Remote Network: ", end="")
    if (endpoint):
        print("Online")
    else:
        print("Offline")
    # print(os.environ)  # shows all en variables
    check_security()


if __name__ == "__main__":
    main()
