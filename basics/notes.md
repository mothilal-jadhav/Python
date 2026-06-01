# Python Fundamentals

## What is Programming?

Programming is the process of describing a sequence of instructions that a computer can execute.

Every program does three things:

1. Stores information
2. Processes information
3. Produces an output

Examples:

Calculator

Input → Numbers
Process → Addition
Output → Result

Instagram

Input → User actions
Process → Backend logic
Output → Feed

Everything is a variation of this pattern.

# How Python Executes Code

Python executes code from top to bottom.

Example

x = 5
print(x)

Output:

5

The interpreter reads each line sequentially.

Think:

Read
Execute
Move Forward

This mental model explains many beginner mistakes.

# Everything is an Object

Python is object-oriented from the beginning.

Examples:

5
"Hello"
[1,2,3]

All are objects.

Objects contain:

- Data
- Behavior

Example:

text = "hello"

text.upper()

The string object contains the method upper().

---

# Comments

Comments are ignored by Python and are for humans to read.

Single-line comment:

```python
# This is a comment
x = 5  # Initialize x
```

Multi-line comment (using strings):

```python
"""
This is a multi-line comment.
It spans several lines.
"""

'''
Another way to write
multi-line comments.
'''
```

### When to use comments

- Explain complex logic
- Document why, not what (the code shows what)
- Mark important sections

Bad comment:

```python
x = x + 1  # add 1 to x
```

Good comment:

```python
# Reset counter after threshold reached
counter = 0
```

---

# Print and Input

### Print function

Output text to the console:

```python
print("Hello, World!")
print(123)
print(True)
```

Multiple arguments:

```python
print("Name:", "Alice", "Age:", 25)
# Output: Name: Alice Age: 25
```

No newline:

```python
print("Hello", end="")
print(" World")
# Output: Hello World
```

### Input function

Get text from the user:

```python
name = input("Enter your name: ")
print("Hello, " + name)
```

Input always returns a string:

```python
age = input("Enter your age: ")
print(type(age))  # <class 'str'>

# Convert to int
age = int(age)
```

---

# Data Types Overview

Python has several built-in data types:

| Type | Example | Mutable |
|------|---------|---------|
| int | `5`, `-10` | No |
| float | `3.14`, `-0.5` | No |
| str | `"hello"` | No |
| bool | `True`, `False` | No |
| list | `[1, 2, 3]` | Yes |
| tuple | `(1, 2, 3)` | No |
| dict | `{"name": "Alice"}` | Yes |
| set | `{1, 2, 3}` | Yes |

### Type conversion

```python
int("123")        # 123
float("3.14")     # 3.14
str(100)          # "100"
list("abc")       # ['a', 'b', 'c']
bool(1)           # True
bool(0)           # False
```

---