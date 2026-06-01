# Conditionals

Control code execution based on conditions.

---

## if Statement

Execute code only if a condition is `True`.

```python
age = 18

if age >= 18:
    print("You are an adult")
```

The indented block runs only when the condition is true.

---

## if-else Statement

Choose between two paths.

```python
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

One block executes if true, the other if false.

---

## if-elif-else Statement

Test multiple conditions sequentially.

```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)  # "C"
```

Only the first matching block executes. Once a condition is true, remaining `elif` statements are skipped.

---

## Nested Conditionals

Conditions inside conditions.

```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Need a license first")
else:
    print("Too young")
```

---

## Comparison Operators

Used to build conditions.

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal | `5 == 5` → True |
| `!=` | Not equal | `5 != 3` → True |
| `>` | Greater than | `5 > 3` → True |
| `<` | Less than | `5 < 3` → False |
| `>=` | Greater or equal | `5 >= 5` → True |
| `<=` | Less or equal | `5 <= 3` → False |

---

## Logical Operators

Combine multiple conditions.

### and — Both must be true

```python
age = 20
has_license = True

if age >= 18 and has_license:
    print("Can drive")
```

### or — At least one must be true

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

### not — Negate

```python
is_raining = False

if not is_raining:
    print("Go outside")
```

---

## Chained Comparisons

Compare against multiple bounds cleanly.

```python
age = 25

if 18 <= age < 65:
    print("Working age")
```

Equivalent to: `if age >= 18 and age < 65:`

---

## Membership Operators

### in

Check if value exists in sequence.

```python
fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("We have apples")
```

### not in

```python
if "grape" not in fruits:
    print("No grapes")
```

With strings:

```python
if "e" in "hello":
    print("Found")
```

With dictionaries (checks keys):

```python
person = {"name": "Alice", "age": 30}

if "name" in person:
    print("Name exists")
```

---

## Identity Operators

### is

Check if two variables reference the same object.

```python
x = [1, 2]
y = [1, 2]
z = x

print(x == y)  # True (same value)
print(x is y)  # False (different objects)
print(x is z)  # True (same object)
```

### is not

```python
if x is not y:
    print("Different objects")
```

Best use case — checking for `None`:

```python
if value is None:
    print("No value provided")

if value is not None:
    process(value)
```

---

## Ternary Operator

Inline if-else for one-line conditionals.

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # "Adult"
```

Format: `value_if_true if condition else value_if_false`

Useful for assigning based on a condition:

```python
max_value = a if a > b else b
message = "Yes" if is_valid else "No"
```

Avoid nesting (hard to read):

```python
# Bad
grade = "A" if x > 90 else "B" if x > 80 else "C"

# Better
if x > 90:
    grade = "A"
elif x > 80:
    grade = "B"
else:
    grade = "C"
```

---

## Truthiness and Falsiness

In boolean context, values are treated as `True` or `False`.

### Falsy values

```python
if 0:           # False
if 0.0:         # False
if "":          # False (empty string)
if []:          # False (empty list)
if {}:          # False (empty dict)
if ():          # False (empty tuple)
if None:        # False
if False:       # False
```

### Truthy values

```python
if 1:           # True
if -1:          # True
if "hello":     # True (non-empty)
if [1, 2]:      # True (non-empty)
if {"a": 1}:    # True (non-empty)
if (1, 2):      # True (non-empty)
if True:        # True
```

### Common patterns

```python
items = [1, 2, 3]

if items:  # True if list is not empty
    process(items)

if not items:  # True if list is empty
    print("No items")

name = user_input or "Guest"  # Use input if truthy, else "Guest"
```

---

## Operator Precedence in Conditions

Order: `not` > `and` > `or`

```python
True or False and False
# Evaluates as: True or (False and False)
#            = True or False
#            = True
```

Use parentheses for clarity:

```python
if (x > 5 and y < 10) or z == 0:
    pass
```

---

## Short-Circuit Evaluation

Operators stop evaluating once result is determined.

```python
# With and: if left is False, right never evaluates
False and expensive_function()

# With or: if left is True, right never evaluates
True or expensive_function()
```

Useful for avoiding errors:

```python
if data and len(data) > 0:  # data is evaluated first
    pass

if users and users[0].is_active():  # Safe
    pass
```

---

## Common Patterns

### Checking valid input

```python
if age >= 0 and age <= 120:
    print("Valid age")
```

### Multiple conditions

```python
if is_admin or is_moderator:
    allow_delete()
```

### Negation for clarity

```python
if not is_error:
    continue_process()
```

### Guard clauses (early return)

```python
def process(data):
    if data is None:
        return
    
    if not isinstance(data, list):
        return
    
    for item in data:
        print(item)
```

### Using defaults

```python
result = value if value else default
result = value or default
```

---

## Best Practices

1. Keep conditions simple

```python
# Bad
if x > 0 and y > 0 and x < 100 and y < 100:
    pass

# Good
is_valid = 0 < x < 100 and 0 < y < 100
if is_valid:
    pass
```

2. Use meaningful names

```python
# Bad
if u:
    pass

# Good
is_user_logged_in = True
if is_user_logged_in:
    pass
```

3. Avoid deep nesting

```python
# Bad (nested 3 levels)
if a:
    if b:
        if c:
            do_it()

# Good (flat, readable)
if a and b and c:
    do_it()
```

4. Use parentheses for complex logic

```python
if (age >= 18 and has_license) or is_supervised:
    can_drive = True
```

---
