# Python Module 02 — Garden Guardian: Data Validation & Error Handling

## Exercises Overview

### Exercise 0: Agricultural Data Validation

Introduces Python data validation and error handling using a simple agricultural sensor scenario as an example.

**Concepts**:
- Converting and validating numeric input using `int()`
- Handling invalid data with `try/except`
- Understanding and catching `ValueError` exceptions
- Allowing the data pipeline to continue after receiving invalid data


### Exercise 1: Agricultural Data Validation Pipeline

Extends the temperature validation process by checking whether values are within a valid range for plants and raising exceptions for out-of-range temperatures.

**Concepts**:

- Validating data against a defined range
- Raising exceptions with `raise`
- Creating custom error messages
- Handling both conversion and validation errors
- Testing boundary values and invalid data

### Exercise 2: Different Types of Problems

Introduces different Python exception types by simulating different kinds of problems.

**Concepts**:
- Handling different exception types
    - ValueError
    - ZeroDivisionError
    - FileNotFoundError
    - TypeError
- Catching multiple exceptions with one try/except
- Continuing execution after an exception

### Exercise 3: Making Your Own Error Types

Introduces custom exception classes and inheritance to handle garden-specific errors.

**Concepts**:

- Creating custom exception classes
- Using inheritance for related errors
- Raising and catching custom exceptions
- Catching multiple custom errors with a parent exception


### Exercise 4: Finally Block - Always Clean Up

Introduces the finally block for guaranteed cleanup after errors.

**Concepts**:

- Using try/except/finally
- Guaranteeing cleanup after errors
- Handling custom exceptions
- Returning from an except block
