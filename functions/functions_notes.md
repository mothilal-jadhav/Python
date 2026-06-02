# Functions

Functions are reusable blocks of code that perform a task. They promote code organization, reusability, and clarity.

---

## Function definition

```python
def function_name(parameters):
    """Docstring explaining the function."""
    body
    return result
```

- Functions are defined with `def`
- Parameters are optional
- Return value is optional (defaults to `None`)

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

---

## Parameters

### Positional parameters

Required parameters passed in order.

```python
def add(a, b):
    return a + b

add(1, 2)
```

### Default parameters

Parameters with default values; order matters (defaults must come after positional).

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")           # uses default
greet("Bob", "Hi")       # overrides default
```

### Keyword arguments

Pass arguments by name, allowing any order.

```python
greet(greeting="Hey", name="Carol")
```

### *args (variable positional arguments)

Collect extra positional arguments as a tuple.

```python
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)  # args = (1, 2, 3, 4)
```

### **kwargs (variable keyword arguments)

Collect extra keyword arguments as a dictionary.

```python
def build_dict(**kwargs):
    return kwargs

build_dict(a=1, b=2)  # {'a': 1, 'b': 2}
```

### Combining all parameter types

Order: positional → default → *args → **kwargs

```python
def full_signature(a, b=2, *args, **kwargs):
    pass
```

---

## Return values

- `return` exits the function and returns a value
- If no `return` is used, the function returns `None`
- You can return multiple values as a tuple

```python
def divmod_custom(a, b):
    return a // b, a % b

quotient, remainder = divmod_custom(10, 3)
```

---

## Scope and variables

- **Local scope**: variables defined inside a function
- **Enclosing scope**: variables in outer functions (for nested functions)
- **Global scope**: module-level variables
- **Built-in scope**: Python built-ins

Lookup order: LEGB (Local → Enclosing → Global → Built-in)

```python
x = 'global'

def outer():
    x = 'enclosing'
    def inner():
        x = 'local'
        print(x)  # local
    inner()
    print(x)  # enclosing

outer()
print(x)  # global
```

### `global` and `nonlocal` keywords

- `global x` — modify a global variable inside a function
- `nonlocal x` — modify an enclosing variable inside a nested function

```python
x = 0

def increment():
    global x
    x += 1

increment()
print(x)  # 1
```

---

## Closures

A nested function that "remembers" variables from its enclosing scope.

```python
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

times_three = make_multiplier(3)
print(times_three(10))  # 30
```

---

## Docstrings

Document your function using triple-quoted strings as the first statement.

```python
def add(a, b):
    """Return the sum of a and b.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        int or float: The sum
    """
    return a + b
```

Accessible via `help(function)` or `function.__doc__`.

---

## Type hints (optional)

Add type annotations for clarity and type checking with tools like mypy.

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

## Lambda functions

Anonymous single-expression functions. Useful for short callbacks.

```python
square = lambda x: x ** 2
print(square(5))  # 25

# Common use: with map, filter, sort
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

Prefer named functions for clarity unless truly one-off.

---

## Decorators (brief introduction)

A function that modifies another function or class. Use with `@` syntax.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

---

## Best practices

- **Single responsibility**: each function should do one thing.
- **Clear names**: choose descriptive function and parameter names.
- **Keep it small**: functions should be concise (typically < 20 lines).
- **Avoid side effects**: prefer pure functions that don't modify global state.
- **Document well**: use docstrings and type hints.
- **Test thoroughly**: write unit tests for complex functions.
- **Use default arguments sparingly**: they can be confusing.
- **Avoid mutable default arguments**: use `None` and create inside the function.

```python
# Bad
def append_to(item, target=[]):
    target.append(item)
    return target

# Good
def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
```

---

## Common patterns

- **Early return**: exit early with error checks
- **Default values**: use sensible defaults to reduce function arguments
- **Unpacking**: `a, b = func()` when returning multiple values
- **Keyword-only arguments**: use `*` to force keyword arguments

```python
def configure(*, debug=False, timeout=30):
    """debug and timeout must be passed as keywords."""
    pass
```

---

## Quick reference

- Define: `def name(params): ...`
- Parameters: positional, default, `*args`, `**kwargs`
- Return: `return value` (or multiple: `return a, b`)
- Scope: LEGB order
- Lambda: `lambda x: expression`
- Decorator: `@decorator_name` above function
- Docstring: first statement in triple quotes
