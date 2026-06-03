# Functional Programming - Interview Notes

## What is Functional Programming?

Functional Programming is a programming paradigm where programs are built using **pure functions** and data is treated as **immutable** as much as possible.

In functional programming, we focus on:

- Functions
- Immutability
- Avoiding side effects
- Function composition
- Higher-order functions
- Declarative style

Interview answer:

> Functional programming is a programming paradigm where computation is treated as the evaluation of functions. It emphasizes pure functions, immutability, avoiding side effects, and writing declarative code.

---

## Why Use Functional Programming?

Functional programming helps with:

- Cleaner code
- Easier testing
- Fewer bugs from changing data
- Better readability
- Easier parallel/concurrent programming
- Reusable functions
- Predictable output

Example:

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, numbers))

print(squares)
```

Output:

```python
[1, 4, 9, 16]
```

---

## Function

A function is a reusable block of code that takes input, performs logic, and returns output.

```python
def add(a, b):
    return a + b
```

Interview answer:

> A function is a block of reusable code that performs a specific task. In functional programming, functions are treated as first-class citizens.

---

## First-Class Functions

In Python, functions are **first-class citizens**.

This means functions can be:

- Assigned to variables
- Passed as arguments
- Returned from another function
- Stored in data structures

Example:

```python
def greet(name):
    return f"Hello, {name}"

message = greet

print(message("Amit"))
```

Interview answer:

> First-class functions mean functions can be treated like regular values. They can be assigned to variables, passed to other functions, and returned from functions.

---

## Higher-Order Functions

A higher-order function is a function that:

- Takes another function as an argument
- Or returns a function

Example:

```python
def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

print(apply_function(square, 5))
```

Output:

```python
25
```

Interview answer:

> A higher-order function is a function that accepts another function as an argument or returns a function as output.

---

## Pure Function

A pure function always gives the same output for the same input and does not cause side effects.

Example:

```python
def add(a, b):
    return a + b
```

This is pure because:

- Same input always gives same output
- It does not modify external data
- It does not print, write files, or change global variables

Interview answer:

> A pure function is a function whose output depends only on its input and which does not modify external state or produce side effects.

---

## Impure Function

An impure function depends on or changes external state.

Example:

```python
total = 0

def add_to_total(value):
    global total
    total += value
    return total
```

This is impure because it modifies a global variable.

Interview answer:

> An impure function is a function that depends on external state or changes external state. Its output may not be predictable only from its inputs.

---

## Pure vs Impure Function

| Pure Function | Impure Function |
|---|---|
| Same input gives same output | Same input may give different output |
| No side effects | Has side effects |
| Easy to test | Harder to test |
| Does not modify external state | May modify external state |
| Example: `add(a, b)` | Example: modifying global variable |

---

## Side Effects

A side effect happens when a function changes something outside itself.

Common side effects:

- Modifying global variables
- Printing output
- Writing to a file
- Updating database
- Changing input data
- Calling external APIs

Example:

```python
def greet(name):
    print(f"Hello, {name}")
```

This has a side effect because it prints output.

Interview answer:

> A side effect is any change a function makes outside its local scope, such as modifying global variables, printing, writing files, or updating a database.

---

## Immutability

Immutability means data cannot be changed after it is created.

Immutable types in Python:

- `int`
- `float`
- `str`
- `tuple`
- `frozenset`
- `bool`

Mutable types in Python:

- `list`
- `dict`
- `set`

Example:

```python
name = "Amit"
name = name.upper()
```

The original string is not modified. A new string is created.

Interview answer:

> Immutability means an object cannot be changed after creation. Functional programming prefers immutable data because it makes code safer and more predictable.

---

## Mutable vs Immutable

| Mutable | Immutable |
|---|---|
| Can be changed | Cannot be changed |
| Example: list, dict, set | Example: int, str, tuple |
| Risk of accidental modification | Safer and predictable |
| Same object can be updated | New object is created |

Example:

```python
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)
```

The list is modified.

```python
name = "amit"
new_name = name.upper()

print(name)
print(new_name)
```

The string is not modified. A new string is created.

---

## Declarative Programming

Declarative programming focuses on **what to do**, not **how to do it**.

Example:

```python
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```

Here, we describe what we want: filter even numbers.

Interview answer:

> Declarative programming focuses on the result we want, while imperative programming focuses on step-by-step instructions.

---

## Imperative vs Declarative

Imperative style:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
```

Declarative style:

```python
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```

Interview answer:

> Imperative programming tells the computer how to do something step by step. Declarative programming tells the computer what result is needed.

---

## Lambda Function

A lambda function is an anonymous function.

Syntax:

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x * x

print(square(5))
```

Output:

```python
25
```

Interview answer:

> A lambda function is a small anonymous function defined using the `lambda` keyword. It is commonly used for short operations with `map`, `filter`, and `sorted`.

---

## Lambda vs Normal Function

| Lambda Function | Normal Function |
|---|---|
| Anonymous | Has a name |
| One expression only | Can have multiple statements |
| Used for short logic | Used for complex logic |
| Created using `lambda` | Created using `def` |

Example:

```python
square = lambda x: x * x
```

Same as:

```python
def square(x):
    return x * x
```

---

## map()

`map()` applies a function to every item in an iterable.

Syntax:

```python
map(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, numbers))

print(squares)
```

Output:

```python
[1, 4, 9, 16]
```

Interview answer:

> `map()` is used to apply a function to each element of an iterable and returns a map object.

---

## filter()

`filter()` filters items based on a condition.

Syntax:

```python
filter(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
```

Output:

```python
[2, 4, 6]
```

Interview answer:

> `filter()` applies a function to each element and keeps only the elements for which the function returns `True`.

---

## reduce()

`reduce()` reduces an iterable to a single value.

It is available in the `functools` module.

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, numbers)

print(total)
```

Output:

```python
10
```

Interview answer:

> `reduce()` repeatedly applies a function to elements of an iterable and reduces them to a single value.

---

## map vs filter vs reduce

| Function | Purpose | Output |
|---|---|---|
| `map()` | Transforms each item | Iterable of transformed values |
| `filter()` | Selects items | Iterable of selected values |
| `reduce()` | Combines items | Single value |

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
total = reduce(lambda a, b: a + b, numbers)
```

---

## List Comprehension

List comprehension is a clean way to create lists.

Example:

```python
numbers = [1, 2, 3, 4]

squares = [x * x for x in numbers]

print(squares)
```

Output:

```python
[1, 4, 9, 16]
```

With condition:

```python
numbers = [1, 2, 3, 4, 5]

even_numbers = [x for x in numbers if x % 2 == 0]
```

Interview answer:

> List comprehension is a concise way to create lists using an expression and optional condition.

---

## map() vs List Comprehension

| map() | List Comprehension |
|---|---|
| Functional style | Pythonic style |
| Uses function | Uses expression |
| Can be less readable with lambda | Usually more readable |
| Returns map object | Returns list directly |

Example:

```python
numbers = [1, 2, 3]

squares1 = list(map(lambda x: x * x, numbers))
squares2 = [x * x for x in numbers]
```

Interview point:

> In Python interviews, list comprehension is often preferred over `map()` with lambda because it is more readable.

---

## Function Composition

Function composition means combining multiple functions to create a new function.

Example:

```python
def double(x):
    return x * 2

def square(x):
    return x * x

result = square(double(3))

print(result)
```

Output:

```python
36
```

Interview answer:

> Function composition means using the output of one function as the input of another function.

---

## Recursion

Recursion is when a function calls itself.

Example:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```python
120
```

Interview answer:

> Recursion is a technique where a function calls itself to solve smaller versions of the same problem. It must have a base condition to stop.

---

## Recursion vs Iteration

| Recursion | Iteration |
|---|---|
| Function calls itself | Uses loops |
| Needs base condition | Needs loop condition |
| Can be elegant | Usually memory efficient |
| Uses call stack | Does not use call stack heavily |

Interview answer:

> Recursion is useful when a problem can be divided into similar subproblems, but iteration is usually more memory efficient in Python.

---

## Closures

A closure is a function that remembers variables from its outer scope even after the outer function has finished.

Example:

```python
def outer(message):
    def inner():
        return message
    return inner

func = outer("Hello")
print(func())
```

Output:

```python
Hello
```

Interview answer:

> A closure is an inner function that captures and remembers variables from its enclosing function scope.

---

## Decorators

A decorator is a function that modifies or extends another function without changing its code.

Example:

```python
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def greet():
    print("Hello")

greet()
```

Interview answer:

> A decorator is a higher-order function that takes another function, adds extra behavior, and returns a new function.

---

## Decorator with Arguments

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(2, 3))
```

Interview point:

> Use `*args` and `**kwargs` in decorators to support functions with different parameters.

---

## Generators

Generators produce values one at a time using `yield`.

Example:

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(3):
    print(num)
```

Interview answer:

> A generator is a function that returns an iterator and produces values lazily using `yield`.

---

## Generator Expression

Generator expression is like list comprehension but lazy.

```python
squares = (x * x for x in range(5))

print(next(squares))
print(next(squares))
```

Interview answer:

> A generator expression creates values lazily, so it is memory efficient for large data.

---

## Iterator

An iterator is an object that can be iterated using `next()`.

It implements:

- `__iter__()`
- `__next__()`

Example:

```python
numbers = iter([1, 2, 3])

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

Interview answer:

> An iterator is an object that returns values one at a time using `__next__()` and remembers its current state.

---

## Iterable vs Iterator

| Iterable | Iterator |
|---|---|
| Can be looped over | Produces next value |
| Has `__iter__()` | Has `__iter__()` and `__next__()` |
| Example: list, tuple, string | Example: object returned by `iter()` |

Example:

```python
numbers = [1, 2, 3]      # iterable
iterator = iter(numbers) # iterator
```

---

## Lazy Evaluation

Lazy evaluation means values are generated only when needed.

Example:

```python
numbers = (x * x for x in range(1000000))
```

The values are not created all at once.

Interview answer:

> Lazy evaluation delays computation until the value is actually needed. It saves memory and improves performance for large datasets.

---

## Currying

Currying means converting a function with multiple arguments into a sequence of functions that each take one argument.

Example:

```python
def add(a):
    def inner(b):
        return a + b
    return inner

add_five = add(5)

print(add_five(3))
```

Output:

```python
8
```

Interview answer:

> Currying transforms a function with multiple arguments into nested functions, each taking one argument.

---

## Partial Function

Partial function fixes some arguments of a function and creates a new function.

Example:

```python
from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)

print(double(5))
```

Output:

```python
10
```

Interview answer:

> A partial function creates a new function by pre-filling some arguments of an existing function.

---

## functools Module

Useful functional programming tools in Python:

- `reduce`
- `partial`
- `lru_cache`
- `wraps`
- `singledispatch`

Example:

```python
from functools import lru_cache

@lru_cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

Interview answer:

> The `functools` module provides higher-order functions and tools useful for functional programming.

---

## itertools Module

`itertools` provides tools for working with iterators.

Common functions:

- `count`
- `cycle`
- `repeat`
- `chain`
- `combinations`
- `permutations`
- `product`

Example:

```python
import itertools

numbers = [1, 2]
letters = ["a", "b"]

result = list(itertools.product(numbers, letters))

print(result)
```

Interview answer:

> `itertools` provides memory-efficient iterator tools for looping, combining, and generating sequences.

---

## zip()

`zip()` combines multiple iterables element by element.

```python
names = ["Amit", "Rahul"]
marks = [85, 90]

result = list(zip(names, marks))

print(result)
```

Output:

```python
[('Amit', 85), ('Rahul', 90)]
```

Interview answer:

> `zip()` combines elements from multiple iterables into tuples.

---

## enumerate()

`enumerate()` gives index and value while looping.

```python
names = ["Amit", "Rahul"]

for index, name in enumerate(names):
    print(index, name)
```

Interview answer:

> `enumerate()` is used when we need both index and value while iterating.

---

## sorted() with key

`sorted()` can use a function as a key.

```python
students = [
    {"name": "Amit", "marks": 85},
    {"name": "Rahul", "marks": 90}
]

sorted_students = sorted(students, key=lambda x: x["marks"])

print(sorted_students)
```

Interview answer:

> The `key` parameter in `sorted()` accepts a function that decides the value used for sorting.

---

## all() and any()

`all()` returns `True` if all values are true.

```python
marks = [80, 90, 70]

print(all(mark >= 35 for mark in marks))
```

`any()` returns `True` if at least one value is true.

```python
marks = [20, 90, 70]

print(any(mark < 35 for mark in marks))
```

Interview answer:

> `all()` checks if all conditions are true, while `any()` checks if at least one condition is true.

---

## Functional Programming vs OOP

| Functional Programming | Object-Oriented Programming |
|---|---|
| Based on functions | Based on classes and objects |
| Prefers immutability | Uses mutable object state |
| Avoids side effects | Encapsulates state and behavior |
| Declarative style | Object modeling style |
| Good for data transformation | Good for real-world entity modeling |

Interview answer:

> Functional programming focuses on pure functions and immutable data, while OOP focuses on objects that combine state and behavior.

---

## Advantages of Functional Programming

- Predictable code
- Easy to test
- Less shared state
- Fewer side effects
- Better for data processing
- Useful in concurrency
- Cleaner transformations

Interview answer:

> Functional programming makes code more predictable because functions depend only on inputs and avoid modifying external state.

---

## Disadvantages of Functional Programming

- Can be harder for beginners
- Too many lambdas can reduce readability
- Recursion can be inefficient in Python
- Python is not purely functional
- Debugging nested function chains can be difficult

Interview answer:

> Functional programming is powerful, but overusing it in Python can make code less readable. Python supports functional programming, but it is not a purely functional language.

---

## Common Interview Questions

### What is functional programming?

Functional programming is a paradigm based on pure functions, immutability, and avoiding side effects.

### What is a pure function?

A pure function always returns the same output for the same input and has no side effects.

### What is a side effect?

A side effect is any change made outside a function, such as modifying global variables, printing, writing files, or updating a database.

### What is immutability?

Immutability means data cannot be changed after creation.

### What is a higher-order function?

A higher-order function takes another function as an argument or returns a function.

### What is lambda in Python?

A lambda is an anonymous function defined using the `lambda` keyword.

### What is the difference between map and filter?

`map()` transforms every element. `filter()` selects elements based on a condition.

### What is reduce?

`reduce()` combines elements of an iterable into a single value.

### What is a closure?

A closure is an inner function that remembers variables from its outer function scope.

### What is a decorator?

A decorator is a function that adds extra behavior to another function without changing its code.

### What is lazy evaluation?

Lazy evaluation means values are computed only when needed.

### What is the difference between iterable and iterator?

An iterable can be looped over. An iterator produces values one at a time using `next()`.

---

## Best Practices

- Prefer pure functions where possible.
- Avoid modifying global variables.
- Avoid unnecessary side effects.
- Use list comprehensions for readability.
- Use lambda only for short logic.
- Use named functions for complex logic.
- Prefer generators for large data.
- Keep functions small and focused.
- Avoid deeply nested functional chains.
- Combine functional and Pythonic style wisely.

---

## Common Mistakes

- Using lambda for complex logic.
- Forgetting that `map()` and `filter()` return iterators in Python 3.
- Overusing `reduce()` when a loop or `sum()` is clearer.
- Modifying input data inside functions.
- Confusing iterable and iterator.
- Forgetting base condition in recursion.
- Writing decorators without `*args` and `**kwargs`.
- Overusing functional programming when simple code is better.

---

## Final Interview Summary

Functional programming is a programming paradigm that focuses on pure functions, immutability, avoiding side effects, and using functions as first-class citizens. Python supports functional programming through features like lambda functions, map, filter, reduce, closures, decorators, generators, comprehensions, and modules like functools and itertools. It is useful for writing predictable, reusable, and testable code, especially for data transformation tasks.