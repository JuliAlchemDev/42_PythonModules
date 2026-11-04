#!/usr/bin/env python3
import sys


def read_file(file_name: str) -> str | None:
    content = None
    try:
        file = open(file_name, "r")
    except (
        PermissionError,
        FileNotFoundError,
        IsADirectoryError
    ) as error:
        print("[STDERR]", file=sys.stderr, end=" ")
        sys.stderr.write(
            f"Error opening file '{file_name}': {error}")
        sys.stderr.write("\n")
    else:
        try:
            content = file.read()
            sys.stdout.write("---\n")
            sys.stdout.write("\n")
            sys.stdout.write(content)
            sys.stdout.write("\n")
            sys.stdout.write("---\n")
        except UnicodeDecodeError as error:
            print("[STDERR]", file=sys.stderr, end=" ")
            sys.stderr.write(
                f"Error reading file '{file_name}': {error}")
            sys.stderr.write("\n")
        finally:
            file.close()
            sys.stdout.write(f"File '{file_name}' closed.")
            sys.stdout.write("\n")
    return content


def transform_and_save(content: str) -> None:
    """
    [] .png ??
    [] should rewrite ??
    """
    is_saved = False
    transform = content.split("\n")
    transformed = "#\n".join(transform)

    sys.stdout.write("\n")
    sys.stdout.write("---")
    sys.stdout.write("\n")
    sys.stdout.write("\n")
    sys.stdout.write(transformed)
    sys.stdout.write("\n")
    sys.stdout.write("---")
    sys.stdout.write("\n")

    try:
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_file = sys.stdin.readline()

        new_file = new_file.strip('\n')
        sys.stdout.write(f"Saving data to '{new_file}'")
        sys.stdout.write("\n")
        sys.stdout.flush()
        if new_file:
            try:
                file = open(new_file, "w")
            except OSError as error:
                print("[STDERR]", file=sys.stderr, end=" ")
                sys.stderr.write(f"Error opening file: {error}")
                sys.stderr.write("\n")
# =============== CHECKING OUT ===============
            else:

                try:
                    file.write(transformed)
                except OSError as error:
                    print("[STDERR]", file=sys.stderr, end=" ")
                    sys.stderr.write(f"Error writing: {error}")
                    sys.stderr.write("\n")
                else:
                    sys.stdout.write(f"Data saved in file '{file.name}'.")
                    sys.stdout.write("\n")
                    sys.stdout.write("\n")
                finally:
                    file.close()
                    # =============== CHECK ME ===============
                    is_saved = True

    except KeyboardInterrupt:
        # should be and error?
        sys.stderr.write("\n")
        print("[STDERR]", file=sys.stderr, end=" ")
        sys.stderr.write("Operation cancelled by user.")

    finally:
        if not is_saved:
            sys.stdout.write("Data not saved.")
            sys.stdout.write("\n")


def main() -> None:
    args = sys.argv
    args_count = len(args)

    if args_count != 2:
        print("[STDERR]", end=" ", file=sys.stderr)
        sys.stderr.write(f"Usage: {args[0]} <file>")
        sys.stderr.write("\n")
        sys.stderr.write("\n")

    else:
        file_name = args[1]
        sys.stdout.write("=== Cyber Archives Recovery & Preservation ===")
        sys.stdout.write("\n")
        sys.stdout.write(f"Accessing file '{file_name}'")
        sys.stdout.write("\n")
        content = read_file(file_name)

        if content is not None:
            sys.stdout.write("\n")
            sys.stdout.write("Transform data:")
            transform_and_save(content)


if __name__ == "__main__":
    main()


# ========== Check this case! ==========
# Enter new file name (or empty):
# Saving data to ''
# Data not saved.

# ========== Check this case! ==========
# Enter new file name (or empty): ^C
# Data not saved.
# [STDERR] Operation cancelled by user.

# ========== Check this case! Linux  ==========
# Enter new file name (or empty): /dev/full
