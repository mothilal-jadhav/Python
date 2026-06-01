# Boolean

A boolean is a data type with exactly two values: `True` or `False`.

---

## Basic Values

```python
is_active = True
is_deleted = False
```

Both `True` and `False` must be capitalized.

---

## Boolean Expressions

Expressions that evaluate to `True` or `False`.

### Comparisons

```python
5 > 3       # True
5 < 3       # False
5 == 5      # True
5 != 3      # True
5 >= 5      # True
5 <= 3      # False
```

### In operator

```python
"a" in "apple"      # True
2 in [1, 2, 3]      # True
```

### Is operator

```python
a = [1, 2]
b = [1, 2]
c = a

a == b      # True
a is b      # False
a is c      # True
```

---

## Logical Operators

### and

Both sides must be `True`:

```python
True and True       # True
True and False      # False
False and False     # False
```

With comparisons:

```python
age = 20
has_license = True

age >= 18 and has_license  # True
```

### or

At least one side must be `True`:

```python
True or False       # True
False or False      # False
True or True        # True
```

With comparisons:

```python
is_weekend = False
is_holiday = True

is_weekend or is_holiday  # True
```

### not

Negates the value:

```python
not True        # False
not False       # True
```

With expressions:

```python
is_logged_in = False
if not is_logged_in:
    print("Please log in")
```

---

## Short-circuit Evaluation

Operators stop evaluating once the result is determined.

### and short-circuit

If left is `False`, right is never evaluated:

```python
False and expensive_function()  # expensive_function() never runs
```

### or short-circuit

If left is `True`, right is never evaluated:

```python
True or expensive_function()  # expensive_function() never runs
```

---

## Truthy and Falsy

In boolean context, non-boolean values are treated as `True` or `False`.

### Falsy values

```python
if 0:           # False
if "":          # False (empty string)
if []:          # False (empty list)
if None:        # False
if False:       # False
```

### Truthy values

```python
if 1:           # True
if "hello":     # True (non-empty string)
if [1, 2]:      # True (non-empty list)
if True:        # True
```

### Usage

```python
items = [1, 2, 3]
if items:  # True if not empty
    process(items)

name = ""
if not name:  # True if empty
    name = "Guest"
```

---

## Boolean Precedence

Order: `not` > `and` > `or`

```python
True or False and False
# Evaluates as: True or (False and False)
#            = True or False
#            = True
```

Use parentheses for clarity:

```python
(True or False) and False  # False
True or (False and False)  # True
```

---

## Common Patterns

### Setting flags

```python
is_valid = True
is_complete = False
```

### Conditional logic

```python
if age >= 18 and country == "USA":
    can_vote = True
```

## Type Checking

```python
type(True)              # <class 'bool'>
isinstance(True, bool)  # True
```

---