# Sets

Sets are unordered collections of unique, hashable elements. They are mutable (except `frozenset`) and useful for membership tests, deduplication, and set algebra.

---

## Creating sets

- Literal from braces: `{1, 2, 3}`
- Empty set must be created with `set()` ( `{}` creates a dict )
- From iterable: `set(iterable)`
- `frozenset(iterable)` creates an immutable set

```python
s = {1, 2, 3}
empty = set()
s_from_list = set([1, 2, 2, 3])  # {1, 2, 3}
fs = frozenset([1,2,3])
```

---

## Basic properties

- Unordered: no index-based access
- Unique elements: duplicates are removed
- Elements must be hashable (e.g., numbers, strings, tuples of immutables)
- Mutable: you can add/remove elements (unless `frozenset`)

---

## Membership and common operations

- `x in s` — membership test (O(1) average)
- `len(s)` — number of elements
- `s.add(x)` — add element
- `s.remove(x)` — remove element, raises `KeyError` if missing
- `s.discard(x)` — remove if present
- `s.pop()` — remove and return an arbitrary element
- `s.clear()` — remove all elements

```python
if 3 in s:
	s.remove(3)
```

---

## Set algebra (methods & operators)

- Union: `s | t` or `s.union(t)`
- Intersection: `s & t` or `s.intersection(t)`
- Difference: `s - t` or `s.difference(t)`
- Symmetric difference: `s ^ t` or `s.symmetric_difference(t)`
- Subset/superset: `s <= t`, `s < t`, `s >= t`, `s > t`

```python
a = {1,2,3}
b = {3,4}
print(a | b)   # {1,2,3,4}
print(a & b)   # {3}
print(a - b)   # {1,2}
```

In-place versions: `s |= t`, `s &= t`, `s -= t`, `s ^= t`.

---

## Set comprehensions

Like list comprehensions but produce sets.

```python
squares = {x*x for x in range(10)}
filtered = {x for x in data if condition(x)}
```

Be careful: comprehensions may drop duplicates and the iteration order is undefined.

---

## `frozenset`

- Immutable and hashable — can be used as dictionary keys or elements of other sets.
- Created with `frozenset(iterable)`.

```python
fs = frozenset([1,2,3])
mapping = {fs: 'value'}
```

---

## Use cases

- Remove duplicates: `unique = set(items)`
- Fast membership checks
- Implement mathematical set operations
- Track visited items (e.g., graph traversal)

---

## Pitfalls and tips

- Sets are unordered — do not rely on insertion order (Python 3.7+ preserves insertion order for dicts but not guaranteed for sets).
- Elements must be hashable. Use tuples instead of lists when you need compound elements.
- Converting back to a list will produce an arbitrary order; sort if order matters: `sorted(s)`.
- For large datasets, consider `frozenset` if you need immutability or hashing.

---

## Performance notes

- Membership (`in`) and add/remove are on average O(1).
- Set operations (union, intersection, difference) are implemented in C and generally fast.
- For small fixed collections, tuples may be more memory-efficient.

---

## Quick reference

- Create: `{1,2}` or `set(iterable)`
- Add: `s.add(x)` — Remove: `s.discard(x)` / `s.remove(x)`
- Union/Intersection/Difference: `|`, `&`, `-`
- Comprehension: `{f(x) for x in iterable if cond}`
- Immutable set: `frozenset(iterable)`

End of sets notes.

