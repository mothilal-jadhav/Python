# Python Notes

> These notes are written for understanding Python deeply, not for memorizing syntax.
>
> The goal is to build accurate mental models so that advanced topics later (OOP, DSA, frameworks, concurrency, etc.) feel natural.

---

# How I Think About Programming

Programming is ultimately about three things:

1. Representing information.
2. Manipulating information.
3. Controlling when and how manipulation happens.

Everything in Python can be reduced to these ideas.

---

# Core Idea

The most important thing to understand:

```python
x = 10
```

This does **not** mean:

> "x contains 10"

A better model is:

```text
x ──> 10
```

Variables are names bound to objects.

Python creates an object and the variable refers to it.

Understanding this explains:

- Assignment
- Mutability
- Function arguments
- Copying objects
- Object-oriented programming

Later, this idea becomes extremely important.

---

# Fundamental Data Types

Everything in Python is an object.

The built-in types are simply the most commonly used object types.

| Type | Purpose |
|--------|----------|
| int | Whole numbers |
| float | Decimal numbers |
| bool | Logical values |
| str | Text |
| list | Ordered mutable collection |
| tuple | Ordered immutable collection |
| set | Collection of unique values |
| dict | Key-value mapping |

These are Python's building blocks.

Almost every program is some combination of them.

---

# Operator Precedence

Python follows mathematical order of operations.

Example:

```python
2 + 3 * 4
```

Result:

```python
14
```

because multiplication happens first.

---

## Practical Order

```text
()
**
* / // %
+ -
comparison
and
or
```

---

## Rule I Actually Follow

If an expression takes more than a few seconds to understand:

```python
result = ((a + b) * c) / d
```

add parentheses.

Readability is more important than remembering precedence rules.

---

# Binary Numbers (`bin()`)

Computers work internally using binary.

The `bin()` function allows inspection of an integer's binary representation.

```python
bin(5)
```

Output:

```python
'0b101'
```

---

Removing the prefix:

```python
bin(5)[2:]
```

Output:

```python
'101'
```

---

Useful when learning:

- Bit manipulation
- Memory representation
- Low-level algorithms

For normal application development, it is rarely needed.

---

# Variables

Variables are references.

Not boxes.

Not containers.

They are **References**.

---

## Assignment

```python
x = 10
```

A name is attached to an object.

---

## Reassignment

```python
x = 10

x = 20
```

The object `10` is not modified.

The reference simply points somewhere else.

---

## Multiple References

```python
a = [1, 2, 3]
b = a
```

Both variables point to the same object.

```text
a ──┐
    ├──► [1,2,3]
b ──┘
```

---

```python
b.append(4)
```

Now:

```python
a
```

returns:

```python
[1,2,3,4]
```

because both names reference the same list.

---

## Naming

Good variable names reduce bugs.

Bad:

```python
x = 25
```

Good:

```python
student_age = 25
```

The code should explain itself.

---

# Expressions vs Statements

A distinction worth understanding.

---

## Expression

Produces a value.

```python
2 + 3
```

Produces:

```python
5
```

More examples:

```python
10 * 2

5 > 3

"Hello" + " World"
```

Everything above evaluates to a value.

---

## Statement

Performs an action.

```python
x = 5
```

```python
print("Hello")
```

```python
if x > 3:
    print("Big")
```

---

## Conditional logic

Conditional logic decides what code runs based on whether one or more conditions are true.

### Basic form

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

- `if` checks the first condition.
- `elif` checks additional conditions only when earlier conditions were false.
- `else` runs when none of the preceding conditions match.

### Boolean expressions

Use comparison operators and logical operators together:

```python
if age >= 18 and has_id:
    can_enter = True
```

- `and` requires both sides to be true.
- `or` requires at least one side to be true.
- `not` reverses the truth value.

### Logical operators

Python has three logical operators: `and`, `or`, and `not`.

#### `and` — both must be true

```python
if age >= 18 and has_license:
    can_drive = True
```

Returns `True` only when both operands are true.

Short-circuit evaluation: if the left side is `False`, the right side is never evaluated.

#### `or` — at least one must be true

```python
if is_weekend or is_holiday:
    no_work = True
```

Returns `True` when at least one operand is true.

Short-circuit evaluation: if the left side is `True`, the right side is never evaluated.

#### `not` — reverses truth value

```python
if not is_logged_in:
    redirect_to_login()
```

Inverts the boolean result.

#### Chaining operators

Combine multiple conditions:

```python
if age >= 13 and age < 18 and not is_banned:
    can_access = True
```

#### Precedence reminder

`not` > `and` > `or`

Use parentheses for clarity:

```python
if (x > 5 and y < 10) or (z == 0):
    process()
```

### Common patterns


```python
if value in collection:
    process(value)

if not items:
    handle_empty()
```

### Best practices

- Keep each condition simple and readable.
- Prefer explicit comparisons over truthy/falsy shortcuts when clarity matters.
- Use parentheses to clarify complex logical expressions.

### Ternary operator

Compact inline conditional:

```python
grade = "Pass" if score >= 60 else "Fail"
```

Form:

```python
value_if_true if condition else value_if_false
```

Use sparingly—avoid nested ternaries since they become hard to read:

```python
# Bad - avoid
status = "A" if x > 90 else "B" if x > 80 else "C"

# Good - use if/elif/else instead
if x > 90:
    status = "A"
elif x > 80:
    status = "B"
else:
    status = "C"
```

---

## Core Idea

Expression:

```text
Produces a value
```

Statement:

```text
Changes state or controls execution
```

---

Most Python code is expressions embedded inside statements.

Example:

```python
age = current_year - birth_year
```

Expression:

```python
current_year - birth_year
```

Statement:

```python
age = ...
```

---

# Augmented Assignment

Shorthand for updating variables.

Instead of:

```python
x = x + 1
```

write:

```python
x += 1
```

---

## Common Operators

```python
+=
-=
*=
/=
%=
**=
//=
```

---

## Why They Exist

Cleaner code.

Compare:

```python
counter = counter + 1
```

vs

```python
counter += 1
```

The second communicates intent immediately.

---

# Strings (`str`)

Strings represent text.

```python
name = "Python"
```

Internally, a string is a sequence of Unicode characters.

---

## Important Property

Strings are immutable.

This means:

```python
name[0] = "J"
```

fails.

---

Operations that appear to modify strings actually create new strings.

```python
name = name.upper()
```

A new string object is returned.

---

## Indexing

```python
text = "Python"

text[0]
```

Output:

```python
'P'
```

---

Negative indexing:

```python
text[-1]
```

Output:

```python
'n'
```

---

## Slicing

```python
text[0:2]
```

Output:

```python
'Py'
```

---

Useful patterns:

```python
text[:3] #Pyt

text[3:] #hon
```

---

## Common Operations

Length:

```python
len(text) #6
```

Concatenation:

```python
"Hello" + " World" #HelloWorld
```

Repetition:

```python
"Ha" * 3 #HaHaHa
```

---

## Useful Methods

```python
lower()
upper()
replace()
split()
count()
startswith()
```

---

## String Formatting

Modern Python uses f-strings.

```python
name = "Sarah"
age = 20

f"{name} is {age} years old"
```

Easy to read.

Easy to maintain.

---

# Boolean (`bool`)

A boolean has only two values.

```python
True
False
```

Used for decision-making.

---

## Comparisons

```python
5 > 3
```

Output:

```python
True
```

---

```python
2 == 4
```

Output:

```python
False
```

---

# Logical Operators

## and

Both sides must be true.

```python
True and True
```

---

## or

At least one side must be true.

```python
True or False
```

---

## not

Flips the result.

```python
not True
```

Output:

```python
False
```

---

# Lists

Lists are dynamic arrays.

Important properties:

```text
Ordered
Mutable
Allow duplicates
Can store mixed types
```

---

## Creation

```python
nums = [1, 2, 3]
```

---

## Adding Data

```python
append()
extend()
insert()
```

---

## Removing Data

```python
remove()
pop()
clear()
```

---

## append vs extend

A common source of mistakes.

```python
nums = [1,2,3]

nums.append([4,5])
```

Result:

```python
[1,2,3,[4,5]]
```

---

```python
nums.extend([4,5])
```

Result:

```python
[1,2,3,4,5]
```

---

## Useful Functions

```python
len()
sum()
min()
max()
sorted()
```

---

## Membership Testing

```python
3 in nums
```

Returns:

```python
True
```

---

## List Unpacking

Assign multiple values at once.

```python
a, b, c = [10,20,30]
```

---

Capturing remaining values:

```python
first, *rest = [1,2,3,4]
```

Result:

```python
first = 1
rest = [2,3,4]
```

---

## Swapping Variables

```python
x, y = y, x
```

One of Python's nicest features.

---

## List Comprehension

A compact way to create lists.

Traditional:

```python
squares = []

for x in range(5):
    squares.append(x*x)
```

---

Pythonic:

```python
squares = [x*x for x in range(5)]
```

Result:

```python
[0,1,4,9,16]
```

---

Think of list comprehensions as:

```text
Generate + Transform + Collect
```

in one expression.

---

## Matrix Using Lists

A matrix is simply:

```python
list[list]
```

Example:

```python
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
```

---

Access row:

```python
matrix[0]
```

---

Access element:

```python
matrix[1][2]
```

Output:

```python
6
```

---

# Dictionaries (`dict`)

Dictionaries are Python's hash tables.

They store:

```text
key → value
```

relationships.

---

Example:

```python
student = {
    "name": "Alice",
    "age": 20
}
```

---

## Why Dictionaries Matter

Fast lookup. # very useful while solving DSA

Average lookup complexity: 

```text
O(1)
```

This is why dictionaries are used everywhere. 

---

## Accessing Values

```python
student["name"] #Alice 
```
but if there is no name section then there will be a error hence to tackle this problem there is a safer way
---

Safer way:

```python
student.get("name") #Alice
```
even if there is no name key/ value then it returns None instead of error
---

Default values:

```python
student.get("city", "N/A")
```

---

## Updating

```python
student["age"] = 21
```

---

```python
student["city"] = "Delhi" # student = {'name' = 'Alice', 'age' = 21, 'city' = 'Delhi"}
```

---

## Useful Methods

```python
keys()
values()
items()
update()
pop()
```

---

## Iteration

```python
for key, value in student.items():
    print(key, value)
```

---

## Dictionary Comprehension

Equivalent of list comprehension for dictionaries.

```python
squares = {
    x: x*x
    for x in range(5)
}
```

Result:

```python
{
    0:0,
    1:1,
    2:4,
    3:9,
    4:16
}
```

---

# Sets

A set is an unordered collection of unique values.

Sets are useful when we need to remove duplicates, test membership quickly, or perform set operations such as union and intersection.

```python
numbers = {1, 2, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4}

empty_set = set()
```

## Basic operations

```python
s = {1, 2, 3}

s.add(4)
print(s)          # {1, 2, 3, 4}

s.remove(2)
print(s)          # {1, 3, 4}

print(3 in s)     # True
```

## Common set methods

- `add(value)` – add a value
- `remove(value)` – remove a value, raises `KeyError` if missing, to tackle this error we use discard
- `discard(value)` – remove a value if present
- `pop()` – remove and return an arbitrary element
- `clear()` – remove all items
- `copy()` – shallow copy of the set

## Set operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)      # union -> {1, 2, 3, 4, 5}
print(a & b)      # intersection -> {3}
print(a - b)      # difference -> {1, 2}
print(a ^ b)      # symmetric difference -> {1, 2, 4, 5}
```

## Notes

- Sets are unordered, so the item order is not preserved.
- Values must be hashable (e.g. numbers, strings, tuples).
- Use sets when uniqueness and membership checks are more important than order.
