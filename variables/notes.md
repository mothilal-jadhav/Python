# Variables
A variable is a name that refers to an object in memory. Think of it as a labeled reference, not a container.

---

## Core Concept: Names vs Objects

### The mental model

```
name ──► object in memory
```

When you write:

```python
x = 10
```

Python creates an integer object with value `10` and binds the name `x` to it.

The variable `x` does **not** contain 10; it **references** an object that has the value 10.

### Why this matters

Understanding this distinction explains:

- Assignment behavior
- Mutability
- Function arguments (pass-by-object-reference)
- Copying behavior
- Object-oriented programming

---

## Creating Variables

### Basic assignment

```python
x = 5
name = "Alice"
price = 19.99
is_active = True
```

### Multiple assignment

Assign the same value to multiple variables:

```python
a = b = c = 0
```

Unpack values from a sequence:

```python
x, y, z = [1, 2, 3]
a, b = ("hello", "world")
```

Unpack with unpacking operator:

```python
first, *rest = [1, 2, 3, 4, 5]
# first = 1
# rest = [2, 3, 4, 5]

a, *middle, z = [1, 2, 3, 4, 5]
# a = 1
# middle = [2, 3, 4]
# z = 5
```

---

## Variable Naming Rules

### Syntax rules

- Must start with a letter (a-z, A-Z) or underscore (`_`)
- Can contain letters, numbers, and underscores
- Cannot contain spaces or special characters
- Case-sensitive: `age`, `Age`, `AGE` are different variables

### Valid names

```python
student_name = "Bob"
_private = 100
age_2024 = 30
MAX_SIZE = 1000
```

### Invalid names

```python
2fast = 10          # Cannot start with a number
my-age = 25         # Cannot use hyphens
my age = 20         # Cannot contain spaces
class = "Math"      # Cannot use reserved keywords
```

---

## Naming Conventions

### Python style (PEP 8)

| Type | Convention | Example |
|------|-----------|---------|
| Variables | snake_case | `student_name`, `total_price` |
| Constants | UPPER_CASE | `MAX_SIZE`, `PI` |
| Private | Leading underscore | `_internal_id` |
| Class methods | snake_case | `calculate_total()` |
| Classes | PascalCase | `StudentClass`, `DataProcessor` |

### Clarity over cleverness

Bad:

```python
x = 25
fn = "Alice"
a, b, c = [1, 2, 3]
```

Good:

```python
student_age = 25
full_name = "Alice"
start, middle, end = [1, 2, 3]
```

---

## Reassignment

Rebinding a variable to a different object:

```python
x = 10
print(x)  # 10

x = 20
print(x)  # 20
```

The original object `10` is not modified; the name `x` simply points elsewhere.

### Reassignment with different types

```python
value = 42           # int
value = "hello"      # str (same name, different object)
value = [1, 2, 3]    # list (same name, different object)
```

---

## References and Identity

### Multiple references to the same object

```python
a = [1, 2, 3]
b = a
```

Both `a` and `b` reference the same list object:

```
a ──┐
    ├──► [1, 2, 3]
b ──┘
```

Modifying through one name affects both:

```python
a.append(4)
print(b)  # [1, 2, 3, 4]
```

### Checking identity

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (same values)
print(a is b)  # False (different objects)
print(a is c)  # True (same object)
```

---

## Variable Scope

The region of code where a variable is accessible.

### Global scope

```python
x = 10  # global variable

def print_x():
    print(x)  # can access global x

print_x()  # 10
```

### Local scope

```python
def my_function():
    y = 5  # local variable
    print(y)

my_function()  # 5
print(y)       # NameError: y is not defined
```

### Global keyword

Modify a global variable inside a function:

```python
x = 10

def increment():
    global x
    x += 1

increment()
print(x)  # 11
```

### Nonlocal keyword

Reference a variable in an enclosing function:

```python
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x += 1
    
    inner()
    print(x)  # 11

outer()
```

---

## Mutable vs Immutable

### Immutable objects

Cannot be changed after creation. Reassignment creates a new object.

```python
x = "hello"
y = x
x = "goodbye"  # new object, x points elsewhere

print(x)  # "goodbye"
print(y)  # "hello" (unchanged)
```

Immutable types: `int`, `float`, `str`, `tuple`, `bool`, `frozenset`

### Mutable objects

Can be modified in place. Changes affect all references.

```python
a = [1, 2, 3]
b = a
a.append(4)  # modify the list in place

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4] (also changed)
```

Mutable types: `list`, `dict`, `set`

---

## Variable Assignment in Functions

### Pass by object reference

Variables are passed by reference to their object, not by value or by reference itself.

```python
def modify_list(lst):
    lst.append(999)  # modifies the original list

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)  # [1, 2, 3, 999]
```

### Immutables appear pass-by-value

```python
def increment(x):
    x = x + 1  # creates new object, doesn't affect original

n = 5
increment(n)
print(n)  # 5 (unchanged)
```

Why? Because `x = x + 1` rebinds `x` to a new object locally.

---

## Variable Deletion

Remove a variable with `del`:

```python
x = 10
print(x)  # 10

del x
print(x)  # NameError: x is not defined
```

The object is only garbage-collected if no other references exist.

---

## Type Checking

### `type()` function

Get the type of a variable:

```python
print(type(5))        # <class 'int'>
print(type("hello"))  # <class 'str'>
print(type([1, 2]))   # <class 'list'>
```

### `isinstance()` function

Check if a variable is an instance of a type:

```python
x = 5
print(isinstance(x, int))        # True
print(isinstance(x, (int, str))) # True (int or str)
```

---

## Variable Inspection

### `id()` function

Get the unique identity of an object:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(id(a))  # e.g., 140234567890
print(id(b))  # e.g., 140234567891 (different)
print(id(c))  # e.g., 140234567890 (same as a)
```

### `dir()` function

List all attributes and methods of an object:

```python
x = "hello"
print(dir(x))  # ['capitalize', 'count', 'find', ...]
```

---

## Common Patterns

### Initialize then use

```python
total = 0
for item in items:
    total += item
```

### Conditional assignment

```python
status = "pass" if score >= 50 else "fail"
```

### Swap variables

```python
a, b = 10, 20
a, b = b, a  # swap using unpacking
print(a, b)  # 20, 10
```

### Default values

```python
user_input = input("Enter name: ") or "Guest"
# If input is empty, use "Guest"
```

---
