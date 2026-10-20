# Python Module 04 — Digital Preservation in the Cyber Archives

## Exercises Overview

### Exercise 0: Ancient Text Recovery

Read a file whose name is given on the command line and display its
contents like `cat`, handling the different failure cases gracefully.

**Concepts**:

- Reading the file name from the command line with `sys.argv` and showing a usage message
- Opening files with `open()`, which returns a file object (`io.TextIOWrapper`), annotated as `typing.IO[str]`
- Reading the contents with `read()` and releasing the file with `close()`
- Handling errors when opening: `FileNotFoundError`, `PermissionError`, `IsADirectoryError`
- Handling errors when reading: `UnicodeDecodeError` (e.g. binary files, images)
- Separating the `open()` and `read()` steps in different `try` blocks, since they fail for different reasons
- Guaranteeing cleanup with `finally`, so the file is closed even if reading fails
