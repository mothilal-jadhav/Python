# Lists

A list is an ordered, mutable collection that can hold items of different types.

---

## Creating Lists

### Basic syntax

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
```

### Empty list

```python
empty = []
my_list = list()
```

### Using list() constructor

```python
chars = list("abc")
print(chars)  # ['a', 'b', 'c']
```

---

## Accessing Elements

### Indexing

Access by position (0-based):

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # "apple"
print(fruits[1])   # "banana"
print(fruits[-1])  # "cherry" (last element)
print(fruits[-2])  # "banana" (second to last)
```

### Slicing

Get a subset of elements:

```python
numbers = [1, 2, 3, 4, 5]

print(numbers[1:4])   # [2, 3, 4] (index 1 to 3)
print(numbers[:3])    # [1, 2, 3] (from start to index 2)
print(numbers[2:])    # [3, 4, 5] (from index 2 to end)
print(numbers[::2])   # [1, 3, 5] (every 2nd element)
print(numbers[::-1])  # [5, 4, 3, 2, 1] (reversed)
```

---

## Modifying Lists

### Assign to index

```python
fruits = ["apple", "banana", "cherry"]
fruits[0] = "orange"
print(fruits)  # ["orange", "banana", "cherry"]
```

### Slice assignment

```python
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [20, 30]
print(numbers)  # [1, 20, 30, 4, 5]
```

---

## Adding Elements

### append()

Add single element at end:

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ["apple", "banana", "cherry"]
```

### extend()

Add multiple elements:

```python
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)  # ["apple", "banana", "cherry", "date"]
```

### insert()

Insert at specific position:

```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")
print(fruits)  # ["apple", "banana", "cherry"]
```

### Concatenation

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]
```

---

## Removing Elements

### remove()

Remove first occurrence of value:

```python
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)  # ["apple", "cherry", "banana"]
```

Raises `ValueError` if not found.

### pop()

Remove and return element by index:

```python
fruits = ["apple", "banana", "cherry"]
last = fruits.pop()
print(last)     # "cherry"
print(fruits)   # ["apple", "banana"]

second = fruits.pop(1)
print(second)   # "banana"
```

### del

Delete by index or slice:

```python
numbers = [1, 2, 3, 4, 5]
del numbers[0]
print(numbers)  # [2, 3, 4, 5]

del numbers[1:3]
print(numbers)  # [2, 5]
```

### clear()

Remove all elements:

```python
numbers = [1, 2, 3]
numbers.clear()
print(numbers)  # []
```

---

## List Methods

### count()

Count occurrences of value:

```python
numbers = [1, 2, 3, 2, 2, 4]
print(numbers.count(2))  # 3
```

### index()

Find first index of value:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # 1
```

Raises `ValueError` if not found.

### sort()

Sort list in place:

```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)  # [1, 1, 3, 4, 5]

# Reverse sort
numbers.sort(reverse=True)
print(numbers)  # [5, 4, 3, 1, 1]
```

### reverse()

Reverse list in place:

```python
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)  # [3, 2, 1]
```

### copy()

Create shallow copy:

```python
original = [1, 2, 3]
copy = original.copy()
copy[0] = 999
print(original)  # [1, 2, 3] (unchanged)
```

---

## List Functions

### len()

Get list length:

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # 3
```

### sorted()

Return sorted copy (doesn't modify original):

```python
numbers = [3, 1, 4, 1, 5]
sorted_list = sorted(numbers)
print(sorted_list)  # [1, 1, 3, 4, 5]
print(numbers)      # [3, 1, 4, 1, 5] (unchanged)
```

### min() and max()

```python
numbers = [3, 1, 4, 1, 5]
print(min(numbers))  # 1
print(max(numbers))  # 5
```

### sum()

```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # 15
```

### reversed()

Return reversed iterator:

```python
numbers = [1, 2, 3]
print(list(reversed(numbers)))  # [3, 2, 1]
```

---

## Checking Membership

### in operator

```python
fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("We have apples")

if "grape" not in fruits:
    print("No grapes")
```

---

## List Comprehension

Create lists concisely:

```python
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

### With conditions

```python
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

### Nested comprehension

```python
matrix = [[x + y for x in range(3)] for y in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
```

---

## Iterating Over Lists

### Basic loop

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### With index

```python
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

Output:
```
0: apple
1: banana
2: cherry
```

### While loop

```python
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

---

## Unpacking

Extract elements into variables:

```python
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)  # 1 2 3

# With star operator
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

# First, middle, last
a, *middle, z = [1, 2, 3, 4, 5]
print(a, middle, z)  # 1 [2, 3, 4] 5
```

---

## Nested Lists

Lists inside lists:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])      # [1, 2, 3]
print(matrix[0][1])   # 2
print(matrix[2][2])   # 9
```

---

## Copying Lists

### Shallow copy

```python
original = [1, 2, 3]
copy = original.copy()

copy[0] = 999
print(original)  # [1, 2, 3]
```

### Deep copy (nested lists)

```python
import copy

original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)

shallow[0][0] = 999
print(original)  # [[999, 2], [3, 4]] (affected)

deep[0][0] = 999
print(original)  # [[999, 2], [3, 4]] (not affected)
```

---

## Common Patterns

### Find element

```python
if 3 in numbers:
    index = numbers.index(3)
    print(f"Found at index {index}")
```

### Remove duplicates (order preserved)

```python
numbers = [1, 2, 2, 3, 1, 4]
unique = list(dict.fromkeys(numbers))
print(unique)  # [1, 2, 3, 4]
```

### Flatten nested list

```python
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6]
```

### Filter elements

```python
numbers = [1, 2, 3, 4, 5]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4]
```

### Transform elements

```python
numbers = [1, 2, 3, 4]
doubled = [x * 2 for x in numbers]
print(doubled)  # [2, 4, 6, 8]
```

---

## Best Practices

1. Use list comprehension for transformations

```python
# Bad
result = []
for x in numbers:
    result.append(x * 2)

# Good
result = [x * 2 for x in numbers]
```

2. Use meaningful variable names

```python
# Bad
lst = [1, 2, 3]

# Good
numbers = [1, 2, 3]
```

3. Prefer `append()` for single additions

```python
# Less efficient
my_list = my_list + [new_item]

# Better
my_list.append(new_item)
```

4. Use `extend()` for multiple additions

```python
# Less efficient
for item in new_items:
    my_list.append(item)

# Better
my_list.extend(new_items)
```

---
