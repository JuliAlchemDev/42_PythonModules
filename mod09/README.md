# Python Module 09 — Discover Pydantic Models & Validation

## Exercises Overview

### Exercise 0: Space Station Data

Create a validated data model for a space station with `BaseModel` and `Field`, and handle validation errors when the data is invalid.

**Concepts**:

- Defining models by inheriting from `BaseModel`
- Field constraints with `Field()`: `min_length`, `max_length`, `ge` and `le`
- Default values (`is_operational: bool = True`) and optional fields (`str | None`)
- Automatic type conversion (e.g. `datetime` fields)
- Catching `ValidationError` and reading its messages with `error.errors()`


### Exercise 1: Alien Contact Logs

Validate alien contact reports with an enum and custom business rules that depend on several fields at once.

**Concepts**:

- Enumerations with `Enum` (and reading their value with `.value`)
- Custom validation of the whole model with `@model_validator(mode="after")`
- Raising `ValueError` inside a validator (Pydantic wraps it in a `ValidationError`)
- Cross-field business rules (contact type vs. witnesses, verification and signal strength)
- Returning `self` from the validator, typed with `typing.Self`

### Exercise 2: Space Crew Management

Model a mission with a nested crew and validate safety rules that depend on the whole crew.

**Concepts**:

- Nested models: a model as the type of another model's field (`list[CrewMember]`)
- Size constraints on lists with `Field(min_length=..., max_length=...)`
- Automatic validation and conversion of nested dictionaries into model instances
- Cross-model validation with `@model_validator(mode="after")` over the whole crew
- Checking collections with `any()` and `all()`
- Cleaning validation messages (removing the `Value error, ` prefix added by Pydantic)


