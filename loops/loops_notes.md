# Loops

Loops repeat code until a condition or sequence is exhausted.

---

## `for` loop

Iterates over any iterable: lists, tuples, strings, sets, dictionaries (keys), `range()`, generators.

### Basic syntax

```python
for item in collection:
    process(item)
```

### Example

```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

### `range()` for numeric loops

```python
for i in range(5):        # 0..4
    print(i)

for i in range(1, 10, 2): # start, stop (exclusive), step
    print(i)
```

### `enumerate()` — index + value

```python
for index, value in enumerate(items, start=0):
    print(index, value)
```

### `zip()` — iterate multiple iterables in parallel

```python
for a, b in zip(list1, list2):
    print(a, b)
```

### Iterating dictionaries

- `.items()` yields (key, value)
- `.keys()` yields keys
- `.values()` yields values

```python
for k, v in d.items():
    print(k, v)
```

---

## `while` loop

Repeat while a condition is true. Use when number of iterations is not known ahead.

### Syntax

```python
while condition:
    body
```

### Example

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### `while True` with `break`

```python
while True:
    data = read()
    if not data:
        break
    process(data)
```

---

## `break`, `continue`, and `else`

- `break` — exit the loop immediately.
- `continue` — skip to the next iteration.
- `else` after a loop runs only if the loop completed normally (no `break`).

```python
for i in range(5):
    if i == 3:
        break
else:
    print("Completed without break")  # Not executed because break ran
```

---

## Comprehensions (compact loops)

Produce new collections concisely.

```python
squares = [x*x for x in range(10)]         # list
evens = [x for x in range(10) if x % 2 == 0]
pairs = [(x, y) for x in range(3) for y in range(3)]
```

Generators (lazy):

```python
g = (x*x for x in range(10))
next(g)
```

Use comprehensions for simple transformations; avoid complex logic inside them.

---

## Iterators and `iter()`/`next()`

Any iterable can produce an iterator with `iter()` and yield values with `next()`.

```python
it = iter([1, 2, 3])
print(next(it))  # 1
print(next(it))  # 2
```

This is useful when you need manual control over iteration.

---