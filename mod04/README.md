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


### Exercise 1: Archive Creation

Transform the contents of a file by adding a special archive character (`#`) at the end of each line, display the transformed content, and optionally save it to a new file.

**Concepts**:

- Reusing the file-reading logic from Exercise 0
- Splitting strings into lines with `split("\n")` and joining them with `join()`
- Transforming text by inserting a special character (`#`) between lines
- Requesting user input with `input()` to choose an output file name
- Opening files in write mode (`"w"`), which creates a new file or truncates an existing one
- Writing transformed content with `write()`
- Handling errors when opening or writing files with `OSError`
- Separating file opening and writing into different `try` blocks, since they can fail independently
- Guaranteeing file closure with `finally`, even if writing fails
- Handling `KeyboardInterrupt` when the user cancels the input with `Ctrl+C`
- Understanding relative paths (`../`) when choosing an output location

### Exercise 2: Stream Management

Adapt the previous exercises to use Python's standard input, output, and error streams. Read user input without using `input()` and route error messages to the standard error stream.

**Concepts**:

- Understanding the three standard streams: `sys.stdin`, `sys.stdout`, and `sys.stderr`
- Using `sys.stdout.write()` instead of `print()` to control output explicitly, including newline characters
- Reading user input with `sys.stdin.readline()` instead of `input()`
- Understanding that `readline()` retains the trailing newline character (`\n`)
- Using `sys.stdout.flush()` to ensure buffered output, such as prompts, is displayed before waiting for input
- Redirecting error messages to `sys.stderr` with `print(..., file=sys.stderr)` or `sys.stderr.write()`
- Understanding the difference between standard output and standard error, and redirecting them independently from the shell (`>`, `2>`)
```bash
# Example:
$ python3 program.py > output.txt 2> errors.txt
```
- Handling `KeyboardInterrupt` when the user cancels an operation with `Ctrl+C`
- Handling errors during file opening, writing, and closing
- Understanding buffering and why a write operation can appear successful even if an error occurs later during `flush()` or `close()`
- Tracking whether data was successfully saved before displaying the final status message

## Debugging: Checking File Closure and Resource Leaks

Three useful debugging techniques when working with files in Python:

**1. Check whether a file is closed**

```python
print(file.closed)
```

- `True`: the file is closed.
- `False`: the file is still open.

**2. Detect unclosed files with ResourceWarning**

Run the script with:

```bash
python3 -W always::ResourceWarning file_name.py
```

Python can issue a `ResourceWarning` when an unclosed file object is garbage-collected.

To force garbage collection during debugging:

```python
import gc
gc.collect()
```

**3. Trace memory allocations with tracemalloc**

```python
import tracemalloc

tracemalloc.start()
```

`tracemalloc` tracks memory allocations and can help investigate memory usage and allocation origins. It does not directly detect unclosed files.

**Note:** These are debugging techniques, not part of the exercise's authorized functions.



