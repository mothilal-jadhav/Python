In order for any programmer to learn a language, there are few key things that we need to really
master for any sort of language, including Python.

-> First are the terms of that language.
    Sometimes a programming language has different words and different definitions for these words that we have to memorize things like **statements, variables, instantiation**.

-> Learn about a languages **data type.**
    That is, what sort of data can a program hold?
    we have different ways to represent values like numbers, letters and symbols.


-> Next, we need to learn about actions at the end of the day.
    Programming is a way for us to tell our machines like Hey, store this data and then retrieve this data and perform some action on it.

# DATA TYPES

- int
- float
- bool
- str
- list
- tuple
- set
- dict

These are the data types.

A data type is a value in Python

int represent all numbers, string will represent all letters and a program is simply instructions that tell a computer what to do.

So the two crucial steps when learning a programming language is that, we have these data types that we need to understand that exist in a language, and then we need to learn how we can manipulate the data, create, store, read, change and remove this data from the machine.

Now these data types are called the fundamental data types.
In Python, they are the core to the language.

after the fundamental data types, we also have something called **classes**
So beyond these data types, we can actually create our own using something called classes.

We also have something called specialized data types.
And these specialized data types they're not built into Python, but they're special packages and modules that we can use from libraries.

lets see some of its examples in the jupiter notebook name Practice where we can see and practise the codes

---

# OPERATOR PRECEDENCE

Think of operator precedence like the **order of operations in math class**. When we have a math problem like `2 + 3 × 4`, we don't just go left to right—you know multiplication comes before addition, so the answer is 14, not 20.

Python follows similar rules! This is super important because it affects what your code actually does.

## The Basic Rules

| Order | Operators | Example | What Happens |
|-------|-----------|---------|--------------|
| **1st** | `()` Parentheses | `(2 + 3) * 4 = 20` | Do what's in parentheses FIRST |
| **2nd** | `**` Exponentiation | `2 ** 3 * 2 = 16` | Power before multiplication |
| **3rd** | `*` `/` `//` `%` | `10 + 2 * 5 = 20` | Multiply/divide before add/subtract |
| **4th** | `+` `-` | `10 + 2 - 3 = 9` | Add/subtract left to right |
| **5th** | Comparisons | `5 > 3 and 2 < 4` | Compare before `and` |
| **6th** | `and` | `True and False or True = True` | `and` before `or` |
| **7th** | `or` | (lowest priority) | Do this last |

**Always use parentheses when unsure!** It makes code clear

# DATA TYPES - `bin`

The `bin()` function converts an integer into a binary string. Computers use binary to represent numbers with only `0` and `1`.

For example:

```python
number = 5
binary_value = bin(number)
print(binary_value)  # Output: 0b101

# If we want to remove the '0b' prefix
binary_digits = bin(number)[2:]
print(binary_digits)  # Output: 101
```

More examples:

```python
print(bin(2))   # Output: 0b10
print(bin(10))  # Output: 0b1010
print(bin(255)) # Output: 0b11111111
```

### note
- `bin()` returns a string starting with `0b`.
- `bin(x)[2:]` gives only the binary digits.
- Use `bin()` when we want to see a number in binary or work with bits.

# Variables

A variable is a name we give to a value so the computer can remember it. Think of it like a labeled box: you put a value inside, and later you can use the box name to get that value.

## How to create a variable

```python
x = 10
name = "Aisha"
price = 25.50
is_student = True
```

In Python:
- `=` means assignment (store a value in a variable)
- The variable name is on the left
- The value is on the right

## Variable rules

- Variable names can use letters, numbers, and underscores: `age_1`, `first_name`
- Names must start with a letter or underscore, not a number
- No spaces are allowed in variable names
- Use lowercase and underscores for simple names: `student_age`

## Why variables are useful

Variables let us reuse values and make code easier to read.

```python
age = 18
message = "You are " + str(age) + " years old"
print(message)
```

## Multiple variables at once

```python
a, b, c = 1, 2, 3
print(a, b, c)

x = y = 5
print(x, y)
```

### note
- Variables can hold any type of data: numbers, text, lists, and more.
- Changing a variable value is easy: `x = 10` then `x = 20`.
- Good variable names makes code much easier to understand.
