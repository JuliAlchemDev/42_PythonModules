#!/usr/bin/env python3


def secure_archive(
        file_name: str,
        mode: str = "r",
        content: str = ""
        ) -> tuple[bool, str]:
    try:
        with open(file_name, mode) as file:
            if mode == "w":
                file.write(content)
                return (True, 'Content successfully written to file')
            else:
                content = file.read()
                return (True, content)

    except OSError as error:
        return (False, str(error))


def main() -> None:
    # ways to handle data[0] == error msg
    fn_name = "secure_archive"

    print("=== Cyber Archives Security ===")

    print(f"\nUsing '{fn_name}' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))

    print(f"\nUsing '{fn_name}' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))

    print(f"\nUsing '{fn_name}' to read from a regular file:")
    data = secure_archive("ancient_fragment.txt", "r")
    print(data)

    print(f"\nUsing '{fn_name}' to write previous content to a new file:")
    print(secure_archive("new_ancient_fragment.txt", "w", data[1]))


if __name__ == "__main__":
    main()
