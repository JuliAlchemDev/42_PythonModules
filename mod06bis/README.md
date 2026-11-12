# Python Module 06bis — Abstract Architecture, from Data Streams to Battle Strategies

## Exercises Overview

### Exercise 3: Entity Factories and Capabilities

Create entities through abstract factories and give some of them an extra ability (transform) through a separate abstract class, exposing only the factories from the `ex3` package.

**Concepts**:

- Abstract classes with `ABC` and `@abstractmethod`
- Concrete methods inside an abstract class (`describe`)
- The abstract factory pattern: `CreatureFactory` with `create_base` and `create_evolved`
- Polymorphism: functions that receive any factory without knowing the concrete classes
- A capability as a separate abstract class that does not inherit from `Creature`
- Multiple inheritance and the method resolution order (`__mro__`)
- Calling each parent `__init__` explicitly when `super()` does not chain them
- Changing behavior through state (`is_transformed` changes what `attack` returns)
- Packages: relative imports and exposing only the factories in `__init__.py`
- Return type hints and `mypy`: concrete factories return a more specific type than `Creature`

## Debugging: Working with Modules and Packages

Useful techniques to inspect a package and test its modules:

**1. Run a single module inside a package**

```bash
python3 -m ex3.factories
```

Run it from the root of the repository. Relative imports only work when the file is loaded as part of the package, not as a loose script.

**2. Check which modules were loaded and what they contain**

```python
import sys
import ex3

print([name for name in sys.modules if name.startswith("ex3")])
print(dir(ex3))
print(dir(sys.modules["ex3.factories"]))
```

**Note:** These are debugging techniques, not part of the exercise's authorized functions.


