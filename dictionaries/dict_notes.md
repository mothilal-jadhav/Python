# Dictionaries

A dictionary is an unordered collection of key-value pairs. It's optimized for fast lookups using keys.

---

## Creating Dictionaries

### Basic syntax

```python
student = {"name": "Alice", "age": 20, "grade": "A"}
```

### Empty dictionary

```python
empty = {}
my_dict = dict()
```

### Using dict() constructor

```python
person = dict(name="Bob", age=25, city="NYC")
```

---

## Accessing Values

### Using keys

```python
student = {"name": "Alice", "age": 20}

print(student["name"])  # "Alice"
print(student["age"])   # 20
```

### get() method

Safe access (returns `None` if key doesn't exist):

```python
print(student.get("name"))        # "Alice"
print(student.get("email"))       # None
print(student.get("email", "N/A")) # "N/A" (default value)
```

---

## Adding and Modifying Values

### Add or update

```python
student = {"name": "Alice", "age": 20}

student["age"] = 21           # Update existing key
student["email"] = "alice@example.com"  # Add new key

print(student)
# {"name": "Alice", "age": 21, "email": "alice@example.com"}
```

### update() method

Update multiple key-value pairs:

```python
student.update({"age": 22, "grade": "A+"})
```

---

## Removing Values

### del keyword

```python
student = {"name": "Alice", "age": 20}

del student["age"]
print(student)  # {"name": "Alice"}
```

Raises `KeyError` if key doesn't exist.

### pop() method

Remove and return value:

```python
age = student.pop("age")
print(age)  # 20

# With default
email = student.pop("email", "no-email@example.com")
```

### popitem() method

Remove and return last key-value pair:

```python
key, value = student.popitem()
```

### clear() method

Remove all items:

```python
student.clear()
print(student)  # {}
```

---

## Dictionary Methods

### keys()

Get all keys:

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

print(student.keys())  # dict_keys(['name', 'age', 'grade'])

for key in student.keys():
    print(key)
```

### values()

Get all values:

```python
print(student.values())  # dict_values(['Alice', 20, 'A'])

for value in student.values():
    print(value)
```

### items()

Get key-value pairs:

```python
print(student.items())
# dict_items([('name', 'Alice'), ('age', 20), ('grade', 'A')])

for key, value in student.items():
    print(f"{key}: {value}")
```

---

## Checking Membership

### in operator

Check if key exists:

```python
student = {"name": "Alice", "age": 20}

if "name" in student:
    print("Name exists")

if "email" not in student:
    print("No email")
```

### Note

`in` checks keys, not values:

```python
print("Alice" in student)  # False (Alice is a value, not a key)
print("name" in student)   # True (name is a key)
```

---

## Dictionary Length

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

print(len(student))  # 3
```

---

## Copying Dictionaries

### Shallow copy

```python
original = {"name": "Alice", "age": 20}
copy = original.copy()

copy["name"] = "Bob"
print(original)  # {"name": "Alice", "age": 20} (unchanged)
```

### Using dict()

```python
copy = dict(original)
```

---

## Nested Dictionaries

Dictionaries inside dictionaries:

```python
company = {
    "name": "TechCorp",
    "employees": {
        "alice": {"age": 30, "dept": "Engineering"},
        "bob": {"age": 25, "dept": "Sales"}
    }
}

print(company["employees"]["alice"]["dept"])  # "Engineering"
```

---

## Dictionary Comprehension

Create dictionaries concisely:

```python
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### With conditions

```python
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

### Transform existing dictionary

```python
original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v * 2 for k, v in original.items()}
print(doubled)  # {"a": 2, "b": 4, "c": 6}
```

---

## Iterating Over Dictionaries

### Iterate over keys

```python
for key in student:
    print(key)
```

### Iterate over key-value pairs

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

### Iterate over values

```python
for value in student.values():
    print(value)
```

---

## setdefault() Method

Set default value if key doesn't exist:

```python
student = {"name": "Alice"}

student.setdefault("age", 20)
print(student)  # {"name": "Alice", "age": 20}

student.setdefault("age", 25)  # Age already exists
print(student)  # {"name": "Alice", "age": 20} (unchanged)
```

---

## fromkeys() Method

Create dictionary with same value for all keys:

```python
keys = ["name", "age", "email"]
user = dict.fromkeys(keys, "N/A")
print(user)  # {"name": "N/A", "age": "N/A", "email": "N/A"}
```

---

## Key Requirements

### Keys must be hashable

Keys must be immutable and hashable. Valid key types:

```python
d = {}
d[1] = "int"
d["string"] = "str"
d[(1, 2)] = "tuple"
d[True] = "bool"
```

Invalid key types (mutable):

```python
d[[1, 2]] = "list"      # TypeError: unhashable type: 'list'
d[{"a": 1}] = "dict"    # TypeError: unhashable type: 'dict'
```

---

## Common Patterns

### Count occurrences

```python
text = "hello"
counts = {}

for char in text:
    counts[char] = counts.get(char, 0) + 1

print(counts)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

### Group by value

```python
students = {"alice": 85, "bob": 85, "charlie": 92}
by_grade = {}

for name, grade in students.items():
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(name)

print(by_grade)  # {85: ['alice', 'bob'], 92: ['charlie']}
```

### Merge dictionaries

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}
print(merged)  # {"a": 1, "b": 2, "c": 3, "d": 4}

# Or (Python 3.9+)
merged = dict1 | dict2
```

### Default values with collections

```python
from collections import defaultdict

counts = defaultdict(int)
for char in "hello":
    counts[char] += 1

print(counts)  # defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 2, 'o': 1})
```

---

## Ordered Dictionaries

Dictionaries maintain insertion order (Python 3.7+).

```python
d = {"z": 1, "a": 2, "m": 3}
print(list(d.keys()))  # ['z', 'a', 'm'] (insertion order)
```

---

## Best Practices

1. Use `.get()` for safe access

```python
# Bad (may raise KeyError)
value = d["key"]

# Good
value = d.get("key", default_value)
```

2. Use meaningful key names

```python
# Bad
d = {1: "Alice", 2: 30}

# Good
d = {"name": "Alice", "age": 30}
```

3. Use dictionary comprehension for transformations

```python
# Bad
result = {}
for x in range(5):
    result[x] = x**2

# Good
result = {x: x**2 for x in range(5)}
```

4. Use `.items()` for key-value iteration

```python
# Less efficient
for key in d:
    value = d[key]

# Better
for key, value in d.items():
    pass
```

---
