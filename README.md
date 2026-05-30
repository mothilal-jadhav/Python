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

---

# Expression vs Statement

These are two different things we see while coding

## What's an Expression?

An **expression** is a piece of code that **produces a value**. It gets evaluated and gives you back a result.

Examples:
```python
5 + 3          # Expression: produces 8
10 * 2         # Expression: produces 20
"hello" + " world"  # Expression: produces "hello world"
3 > 2          # Expression: produces True
```

Key point: Expressions can be used anywhere a value is expected.

## What's a Statement?

A **statement** is an instruction that **does something** but doesn't necessarily give you back a value. It tells Python to take an action.

Examples:
```python
x = 5          # Statement: assigns 5 to x
print("Hi")    # Statement: prints something to screen
if x > 3:      # Statement: conditional instruction
    print("x is bigger")
```

Key point: Statements perform actions.

## The Main Difference

```python
# EXPRESSION - produces a value
result = 2 + 3         # The 2 + 3 part is an expression
print(2 + 3)           # 2 + 3 is an expression, gives 5

# STATEMENT - does something
x = 10                 # This is a statement (assignment)
if x > 5:              # This is a statement (conditional)
    print("x is big")  # This is a statement (function call)
```

## Real example to see the difference

```python
# Expression inside a statement
age = 18 + 2           # (18 + 2) is an expression, = is a statement
print(age * 2)         # age * 2 is an expression, print() is a statement

# Can't do this (wrong!)
5 + 3 = x              # Error! Expression can't be on the left side

# This works (right!)
x = 5 + 3              # Statement with an expression inside
```

## Why this matters

- **Expressions** are used to calculate or compare values
- **Statements** are used to make things happen or change state
- Many statements contain expressions inside them
- Understanding this helps us debug when something doesn't work as expected

---

# Augmented Assignment Operators

Augmented assignment operators are shortcuts that combine an operation with assignment. Instead of writing `x = x + 5`, you can write `x += 5`. They make your code cleaner and more readable.

## Common Augmented Assignment Operators

| Operator | Example | Equivalent to | What it does |
|----------|---------|---------------|--------------|
| `+=` | `x += 5` | `x = x + 5` | Add and assign |
| `-=` | `x -= 3` | `x = x - 3` | Subtract and assign |
| `*=` | `x *= 2` | `x = x * 2` | Multiply and assign |
| `/=` | `x /= 4` | `x = x / 4` | Divide and assign |
| `//=` | `x //= 2` | `x = x // 2` | Floor divide and assign |
| `%=` | `x %= 3` | `x = x % 3` | Modulo and assign |
| `**=` | `x **= 2` | `x = x ** 2` | Exponentiate and assign |

## Examples

### Addition and subtraction
```python
count = 10
count += 5        # count is now 15
count -= 3        # count is now 12
print(count)      # Output: 12
```

### Multiplication and division
```python
price = 100
price *= 1.1      # Increase by 10% (multiply by 1.1)
print(price)      # Output: 110.0

price /= 2        # Cut in half
print(price)      # Output: 55.0
```

### With strings
```python
message = "Hello"
message += " World"    # Concatenate
print(message)         # Output: Hello World

text = "ab"
text *= 3              # Repeat 3 times
print(text)            # Output: ababab
```

### With lists
```python
my_list = [1, 2, 3]
my_list += [4, 5]      # Add more items
print(my_list)         # Output: [1, 2, 3, 4, 5]
```

## Why use augmented operators?

1. **Shorter code**: `x += 1` is cleaner than `x = x + 1`
2. **Less repetition**: You don't repeat the variable name
3. **Faster to type**: Once you're used to them, they're quicker
4. **Same meaning**: Everyone knows what `+=` means

## Example comparison

```python
# Without augmented operators
score = 0
score = score + 10
score = score + 5
score = score * 2
print(score)  # Output: 30

# With augmented operators (same result, cleaner code)
score = 0
score += 10
score += 5
score *= 2
print(score)  # Output: 30
```

## Things to remember

- Augmented operators work with all data types that support the operation (numbers, strings, lists, etc.)
- They always modify the original variable—there's no new variable created
- Use them when you're updating a variable with an operation
