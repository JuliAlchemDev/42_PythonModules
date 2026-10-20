#!/usr/bin/env python3
import sys
import typing


def read_file(file: typing.IO[str]) -> None:
    content = file.read()
    print("---\n")
    print(content)
    print("---")


def main() -> None:
    args = sys.argv
    args_count = len(args)

    if args_count != 2:
        print(f"Usage: {args[0]} <file>")
    else:
        file_name = args[1]
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{file_name}'")

        try:
            file = open(file_name)
        except (
            PermissionError,
            FileNotFoundError,
            IsADirectoryError
                ) as error:
            print(f"Error opening file '{file_name}': {error}", "\n")
        else:
            try:
                read_file(file)
            except UnicodeDecodeError as error:
                print(f"Error reading file '{file_name}': {error}", "\n")
        finally:
            file.close()
            print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
