#!/usr/bin/env python3
import sys
# import typing


def read_file(file_name: str) -> str | None:
    content = None
    try:
        file = open(file_name, "r")
    except (
        PermissionError,
        FileNotFoundError,
        IsADirectoryError
    ) as error:
        print(f"Error opening file '{file_name}': {error}")
    else:
        try:
            content = file.read()
            print("---\n")
            print(content)
            print("---")
        except UnicodeDecodeError as error:
            print(f"Error reading file '{file_name}': {error}", "\n")
        finally:
            file.close()
            print(f"File '{file_name}' closed.")
    return content


def transform_and_save(content: str) -> None:
    transform = content.split("\n")
    transformed = "#\n".join(transform)

    print("---\n")
    print(transformed)
    print("---")

    try:
        new_file = input("Enter new file name (or empty): ")
        if new_file:
            try:
                file = open(new_file, "w")
            except OSError as error:
                print(f"Error opening file: {error}", "\n")

            else:
                try:
                    print(f"Saving data to '{new_file}'")
                    file.write(transformed)
                except OSError as error:
                    print(f"Error writing: {error}", "\n")
                else:
                    print(f"Data saved in file '{file.name}'.")
                finally:
                    file.close()
        else:
            print("Not saving data.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")


def main() -> None:
    args = sys.argv
    args_count = len(args)

    if args_count != 2:
        print(f"Usage: {args[0]} <file>")
    else:
        file_name = args[1]
        print("=== Cyber Archives Recovery & Preservation ===")

        print(f"Accessing file '{file_name}'")
        content = read_file(file_name)

        if content is not None:
            print("\nTransform data:")
            transform_and_save(content)


if __name__ == "__main__":
    main()
