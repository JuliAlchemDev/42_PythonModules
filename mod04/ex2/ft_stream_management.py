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
            f"Error opening file '{file_name}': {error}"
            )
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
                f"Error reading file '{file_name}': {error}"
                )
            sys.stderr.write("\n")
        finally:
            file.close()
            sys.stdout.write(f"File '{file_name}' closed.")
            sys.stdout.write("\n")
            sys.stdout.write("\n")
    return content


def transform_and_save(content: str) -> None:
    pass


def main() -> None:
    args = sys.argv
    args_count = len(args)

    if args_count != 2:
        print("[STDERR]", end=" ", file=sys.stderr)
        sys.stderr.write(f"Usage: {args[0]} <file>")
        sys.stderr.write("\n")

    else:
        file_name = args[1]
        sys.stdout.write("=== Cyber Archives Recovery & Preservation ===")
        sys.stdout.write("\n")
        sys.stdout.write(f"Accessing file '{file_name}'\n")
        sys.stdout.write("\n")
        content = read_file(file_name)

        if content is not None:
            sys.stdout.write("\n")
            sys.stdout.write("Transform data:")
            transform_and_save(content)


if __name__ == "__main__":
    main()
