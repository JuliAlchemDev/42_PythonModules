import sys
import os
import site


def main() -> None:
    global_py = sys.base_prefix
    used_py = sys.prefix

    has_venv = used_py != global_py
    active_interpreter = sys.executable
    how_to_msg = "To seal the laboratory, run:\n" \
        "python3 -m venv lab_env\n" \
        "source lab_env/bin/activate # On Unix\n" \
        "lab_env\\Scripts\\activate # On Windows\n" \
        "\n" \
        "Then run this program again."

    if (has_venv):
        status = "The laboratory is sealed"
        venv = os.path.basename(sys.prefix)
        msg = "SUCCESS: You are working in an isolated environment!\n" \
            "Safe to install reagents without affecting\n" \
            "the global system.\n"
        reagent_path = site.getsitepackages()[0]

    else:
        status = "You are working in the open"
        venv = "None detected"
        msg = "WARNING: You are in the global environment!\n" \
            "Every reagent you install here leaks into the whole system.\n"

    print(f"\nLABORATORY STATUS: {status}\n")
    print(f"Current Python: {active_interpreter}")
    print(f"Virtual Environment: {venv}")
    if (has_venv):
        print(f"Environment Path: {used_py}")

    print()
    print(msg)

    if (has_venv):
        print("Reagent installation path:")
        print(reagent_path)
    else:
        print(how_to_msg)


if __name__ == "__main__":
    main()
