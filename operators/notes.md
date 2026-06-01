# Operators

Operators are symbols that perform operations on values and variables.

---

## Arithmetic Operators

Used for mathematical calculations.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `6 / 3` | `2.0` |
| `//` | Floor division | `7 // 2` | `3` |
| `%` | Modulo (remainder) | `7 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### Examples

```python
print(10 + 5)      # 15
print(10 - 5)      # 5
print(10 * 5)      # 50
print(10 / 5)      # 2.0
print(10 // 3)     # 3 (floor division)
print(10 % 3)      # 1 (modulo)
print(2 ** 8)      # 256 (2 to the power of 8)
```

---

## Comparison Operators

Compare values and return `True` or `False`.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal | `5 == 5` | `True` |
| `!=` | Not equal | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater or equal | `5 >= 5` | `True` |
| `<=` | Less or equal | `5 <= 3` | `False` |

### Examples

```python
print(10 == 10)    # True
print(10 != 5)     # True
print(10 > 5)      # True
print(10 < 5)      # False
print(10 >= 10)    # True
print(10 <= 5)     # False
```

### Chaining comparisons

```python
x = 5
print(1 < x < 10)  # True (equivalent to 1 < x and x < 10)
```

---

## Logical Operators

Combine boolean values using `and`, `or`, `not`.

### `and` — both must be true

```python
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False
```

Short-circuits: if left is `False`, right is not evaluated.

### `or` — at least one must be true

```python
print(True or False)    # True
print(False or False)   # False
```

Short-circuits: if left is `True`, right is not evaluated.

### `not` — negation

```python
print(not True)         # False
print(not False)        # True
```

### Examples

```python
age = 20
has_license = True

if age >= 18 and has_license:
    print("Can drive")

if age < 13 or age > 65:
    print("Eligible for discount")

if not is_logged_in:
    redirect_to_login()
```

---

## Assignment Operators

Assign or update values.

| Operator | Example | Equivalent to |
|----------|---------|---------------|
| `=` | `x = 5` | Assign |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

### Examples

```python
x = 10
x += 5      # x is now 15
x -= 3      # x is now 12
x *= 2      # x is now 24
x /= 4      # x is now 6.0
x //= 2     # x is now 3.0
x %= 2      # x is now 1.0
x **= 2     # x is now 1.0
```

---

## Identity Operators

Check if two variables reference the same object.

| Operator | Name | Example | Meaning |
|----------|------|---------|---------|
| `is` | Identity | `a is b` | Same object in memory |
| `is not` | Not identity | `a is not b` | Different objects |

### Examples

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)      # True (same value)
print(a is b)      # False (different objects)
print(a is c)      # True (same object)
```

### Best practice

Use `is` for `None` checks:

```python
if value is None:
    handle_none()

if value is not None:
    process(value)
```

---

## Membership Operators

Check if a value exists in a sequence.

| Operator | Example | Meaning |
|----------|---------|---------|
| `in` | `x in list` | Value is in sequence |
| `not in` | `x not in list` | Value is not in sequence |

### Examples

```python
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)      # True
print("grape" in fruits)      # False
print("grape" not in fruits)  # True

text = "hello"
print("h" in text)            # True
print("x" in text)            # False
```

With dictionaries:

```python
person = {"name": "Alice", "age": 30}

print("name" in person)       # True (checks keys)
print("Alice" in person)      # False (Alice is a value, not a key)
```

---

## Bitwise Operators

Operate on binary representations of integers.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `&` | AND | `5 & 3` | `1` |
| `|` | OR | `5 | 3` | `7` |
| `^` | XOR | `5 ^ 3` | `6` |
| `~` | NOT | `~5` | `-6` |
| `<<` | Left shift | `5 << 1` | `10` |
| `>>` | Right shift | `5 >> 1` | `2` |

### Examples

```python
a = 5      # Binary: 0101
b = 3      # Binary: 0011

print(a & b)       # 1 (0001)
print(a | b)       # 7 (0111)
print(a ^ b)       # 6 (0110)
print(~a)          # -6
print(a << 1)      # 10 (1010, shifted left)
print(a >> 1)      # 2 (0010, shifted right)
```

### Use cases

- Manipulating flags
- Optimizing performance in specific algorithms
- Working with binary protocols
- Rare in typical application code

---

## Operator Precedence

Order in which operators are evaluated (high to low):

1. `()` — Parentheses
2. `**` — Exponentiation
3. `+x`, `-x`, `~x` — Unary operators
4. `*`, `/`, `//`, `%` — Multiplication, division, modulo
5. `+`, `-` — Addition, subtraction
6. `<<`, `>>` — Bitwise shifts
7. `&` — Bitwise AND
8. `^` — Bitwise XOR
9. `|` — Bitwise OR
10. `==`, `!=`, `<`, `>`, `<=`, `>=`, `in`, `not in`, `is`, `is not` — Comparisons
11. `not` — Logical NOT
12. `and` — Logical AND
13. `or` — Logical OR

### Examples

```python
# Without parentheses (follows precedence)
result = 2 + 3 * 4     # 2 + 12 = 14

# With parentheses (explicit)
result = (2 + 3) * 4   # 5 * 4 = 20

# Complex expression
result = 5 > 3 and 2 < 4 or False
# Evaluates as: (5 > 3) and (2 < 4) or False
#            = True and True or False
#            = True or False
#            = True
```

### Rule of thumb

When in doubt, use parentheses. It's better to be explicit than to rely on precedence rules.

---

## String Operators

### Concatenation

```python
a = "Hello"
b = "World"
result = a + " " + b   # "Hello World"
```

### Repetition

```python
text = "Ha" * 3         # "HaHaHa"
```

### Membership

```python
"ell" in "Hello"        # True
"xyz" not in "Hello"    # True
```

---

## Ternary Operator (Conditional Expression)

Inline conditional expression.

```python
value_if_true if condition else value_if_false
```

### Example

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # "Adult"

score = 75
grade = "Pass" if score >= 50 else "Fail"
```

### Caution

Avoid nesting ternary operators as they reduce readability:

```python
# Avoid
grade = "A" if x > 90 else "B" if x > 80 else "C"

# Prefer
if x > 90:
    grade = "A"
elif x > 80:
    grade = "B"
else:
    grade = "C"
```

---

## Walrus Operator `:=` (Assignment Expression)

Introduced in Python 3.8. Assigns a value and returns it in a single expression.

### Example

```python
# Without walrus operator
data = read()
if data:
    process(data)

# With walrus operator
if (data := read()):
    process(data)
```

### Use case

Useful in comprehensions and loops where assignment and condition are closely related:

```python
# List comprehension with walrus
results = [y for x in range(10) if (y := x * 2) > 5]
```

---