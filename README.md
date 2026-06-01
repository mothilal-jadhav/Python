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

Augmented assignment operators are shortcuts that combine an operation with assignment. Instead of writing `x = x + 5`, i can write `x += 5`. They make our code cleaner and more readable.

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

## Things to remember

- Augmented operators work with all data types that support the operation (numbers, strings, lists, etc.)
- They always modify the original variable—there's no new variable created
- Use them when you're updating a variable with an operation

---

# Data Types -  String

A **string** is text data. It can contain letters, numbers, spaces, and symbols. In Python, we create a string by putting text inside quotes (single or double).

## Creating Strings

```python
name = "Alice"
greeting = 'Hello'
message = "Python is awesome!"
empty = ""
```

Both single and double quotes work the same way.

## Common String Operations

### Concatenation (joining strings)
```python
first = "Hello"
second = "World"
result = first + " " + second
print(result)  # Output: Hello World
```

### Repetition (repeating strings)
```python
word = "Ha"
laugh = word * 3
print(laugh)  # Output: HaHaHa
```

### Length (counting characters)
```python
text = "Python"
print(len(text))  # Output: 6
```

### Accessing characters (indexing)
```python
word = "Code"
print(word[0])  # Output: C (first character)
print(word[2])  # Output: d (third character)
print(word[-1]) # Output: e (last character)
```

### Slicing (getting parts of a string)
```python
text = "Python"
print(text[0:2])   # Output: Py (characters 0 and 1)
print(text[1:4])   # Output: yth
print(text[:3])    # Output: Pyt (from start to index 2)
print(text[3:])    # Output: hon (from index 3 to end)
```

## Useful String Methods

```python
text = "Hello World"

print(text.lower())        # Output: hello world
print(text.upper())        # Output: HELLO WORLD
print(text.replace("World", "Python"))  # Output: Hello Python
print(text.split())        # Output: ['Hello', 'World']
print(text.startswith("Hello"))  # Output: True
print(text.count("l"))     # Output: 3
```

## String Formatting

```python
name = "Sarah"
age = 20

# Using f-strings (modern way)
message = f"{name} is {age} years old"
print(message)  # Output: Sarah is 20 years old

# Using format()
message = "{} is {} years old".format(name, age)
print(message)  # Output: Sarah is 20 years old
```

## Things to Remember

- Strings are immutable, we can't change a character directly
- Indexing starts at 0; negative numbers count from the end
- String methods don't change the original string; they return a new one
- Use f-strings for easy variable insertion into strings

---

# Data Types - Boolean

A **Boolean** is a simple data type with only two values: `True` or `False`.

Booleans are often used for conditions, decisions, and checks.

```python
is_raining = False
is_sunny = True

print(is_raining)  # Output: False
print(is_sunny)    # Output: True
```

## Boolean expressions

A Boolean expression compares values or checks conditions, and it returns either `True` or `False`.

```python
print(5 > 3)       # Output: True
print(2 == 4)      # Output: False
print(10 <= 10)    # Output: True
print("hi" != "hello")  # Output: True
```

## Boolean logic

```python
print(True and False)  # Output: False
print(True or False)   # Output: True
print(not True)        # Output: False
```

## Things to remember

- `True` and `False` are capitalized in Python
- Use Booleans to store yes/no, on/off, pass/fail style values
- Boolean expressions are used in `if` statements and loops

# DATA TYPE - Lists
A **list** is an ordered collection that can hold items of different types. Lists are mutable — we can change them after creation.

## Creating lists

```python
nums = [1, 2, 3]
mix = [1, "two", 3.0, True]
empty = []
```

## Access & modify

```python
print(nums[0])    # Output: 1
nums[1] = 20      # change second item
nums.append(4)    # add at end
nums.pop()        # remove last item
```

## Useful operations

```python
print(len(nums))      # length
print(nums[1:3])      # slicing
print(2 in nums)      # membership test
```

## list comprehension

```python
squares = [x*x for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

### Things to remember
- Lists are ordered and mutable.
- Use `append`, `insert`, `remove`, `pop` to change lists.
- List comprehensions are a compact way to build lists.
