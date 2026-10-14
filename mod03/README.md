# Python Module 03 — Mastering Python Collections

## Exercises Overview

### Exercise 0: Command Quest

Receive and process arguments provided through the command line using the `sys module`.

**Concepts**:
- Importing and using the sys module
- Command-line arguments with sys.argv
- Lists and list indexing
- Iterating through list elements with a for loop

### Exercise 1: Score Cruncher

Filter and convert command-line arguments into integers, handle invalid input, and calculate basic statistics.

**Concepts**:
- Processing command-line arguments with sys.argv
- Creating and manipulating lists
- Exception handling with try/except
- Basic statistics with sum(), len(), max(), and min()
- Calculating averages and ranges
- Filtering invalid data while processing input


### Exercise 2: Position Tracker

Store and manage 3D coordinates using tuples, validate user input with exception handling, and calculate distances.

**Concepts**:

- Storing structured data with tuples
- Tuple packing and unpacking (`x, y, z = coordinates`)
- Getting user input with input() and parsing it with str.split()
- Exception handling with try/except for invalid numeric input
- Retrying input until valid data is provided
- Using functions to encapsulate and return reusable logic

### Exercise 3: Achievement Hunter

Use sets to store unique achievements and analyze them across players.

**Concepts**:

- Sets: unordered collections of unique elements
- Creating sets with `set()` (and why an empty set prints as `set()`, not `{}`)
- Set operations: `union()`, `intersection()` and `difference()`
- Random selection with the `random` module (`random.choices()`, `random.randint()`)

### Exercise 5: Stream Wizard

Generate and consume data streams on demand with generators.

**Concepts**:

- Generators and the `yield` keyword
- Infinite generators and lazy evaluation (memory efficiency)
- Pulling values manually with `next()`
- Consuming a generator directly in a `for` loop
- Type hints for generators with `typing.Generator`


### Exercise 6: Data Alchemist

Transform and filter data with list and dictionary comprehensions.

**Concepts**:

- List comprehensions: transforming and filtering (`[expr for x in items if cond]`)
- Dictionary comprehensions (`{key: value for ...}`)
- Comprehensions on sets (`{x for x in ...}`)
- Filtering with `if` at the end vs. transforming with `if ... else` at the start
- Building a new collection from another (equivalent to a `for` loop with `append`)
