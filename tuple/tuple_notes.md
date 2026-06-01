# Tuples

Tuples are immutable, ordered sequences used to store heterogeneous data. They are similar to lists but cannot be changed after creation.

---

## Creating tuples

- Literal: `(1, 2, 3)`
- Empty tuple: `()`
- Single-element tuple: `(value,)` — the trailing comma is required
- From iterable: `tuple(iterable)`

```python
t = (1, 'a', 3.14)
empty = ()
single = ('only',)
t_from_list = tuple([1, 2, 3])
```

---

## Packing and unpacking

Tuple packing assigns multiple values to one tuple; unpacking extracts them.

```python
packed = 1, 2, 3         # packing
a, b, c = packed         # unpacking
head, *rest = [1,2,3,4]  # starred expression
```

---

## Accessing elements

- Indexing: `t[0]`, `t[-1]`
- Slicing: `t[1:3]`
- Immutability: assignment like `t[0] = x` raises `TypeError`.

```python
names = ('Alice', 'Bob', 'Carol')
print(names[1])   # 'Bob'
print(names[1:])  # ('Bob', 'Carol')
```

---

## Useful operations

- Concatenate: `t1 + t2`
- Repeat: `t * n`
- Membership: `x in t`
- Length: `len(t)`
- `t.count(value)` and `t.index(value)`

```python
t = (1, 2)
t2 = t + (3,)
print(t2 * 2)     # (1, 2, 3, 1, 2, 3)
```

---

## When to use tuples

- Fixed collections of items (e.g., coordinates, config constants).
- As dictionary keys (immutable and hashable) when elements themselves are hashable.
- When you want to signal immutability to callers.

---

## Performance notes

- Tuples are usually slightly more memory- and CPU-efficient than lists for small fixed collections.
- Use tuples for heterogeneous records; use lists for homogeneous, resizable collections.

---
