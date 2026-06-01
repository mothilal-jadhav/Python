# Strings

Strings (`str`) are immutable sequences of Unicode characters and are the primary text type in Python.

---

## Creating strings

- Single quotes: `'hello'`
- Double quotes: `"hello"`
- Triple quotes for multi-line: `'''multi\nline'''` or `"""multi\nline"""`
- Raw strings (no backslash escapes): `r"C:\\path"` (useful for regex and paths)

```python
s = 'hello'
multiline = """Line1
Line2"""
raw = r"\n"  # two characters: backslash + n
```

---

## Immutability and common operations

- Strings are immutable: methods return new strings.
- Concatenate: `s1 + s2`
- Repeat: `s * 3`
- Length: `len(s)`
- Indexing: `s[0]`, `s[-1]`
- Slicing: `s[start:stop:step]`

```python
s = "hello"
print(s[1:4])  # 'ell'
print(s[::-1])  # reversed
```

---

## f-strings and formatting

- f-strings (Python 3.6+): `f"name={name!r}"` — fast and readable.
- Format method: `"{:.2f}".format(x)`
- Percent formatting (older): `"%s %d" % (s, n)`

```python
name = 'Alice'
age = 30
print(f"{name} is {age} years old")
print("{:.2f}".format(3.14159))
```

Formatting options: alignment, width, precision, type (d, f, s, b, x).

---

## Common string methods

- `str.split(sep=None, maxsplit=-1)` — split into list
- `sep.join(iterable)` — join strings with separator
- `str.strip(chars=None)` — trim whitespace (or chars)
- `str.replace(old, new, count=-1)` — replace substrings
- `str.find(sub)` / `str.rfind(sub)` — return -1 if not found
- `str.index(sub)` / `str.rindex(sub)` — raise ValueError if not found
- `str.startswith(prefix)` / `str.endswith(suffix)`
- `str.lower()` / `str.upper()` / `str.title()` / `str.capitalize()`
- `str.isalpha()` / `str.isdigit()` / `str.isnumeric()` / `str.isalnum()` / `str.isspace()`

```python
s = '  Hello, world!  '
words = s.strip().split(',')
joined = ' - '.join(words)
print(joined)
```

---

## Encoding and bytes

- `str.encode(encoding='utf-8')` → `bytes`
- `bytes.decode(encoding='utf-8')` → `str`
- Use explicit encodings when reading/writing files or network communication.

```python
txt = 'café'
bs = txt.encode('utf-8')
print(bs)            # b'caf\xc3\xa9'
print(bs.decode())   # 'café'
```

---

## Performance and patterns

- Use `.join()` to build large strings from parts — faster than repeated concatenation in a loop.
- For many small writes, consider `io.StringIO` as a mutable buffer.
- Prefer built-in functions (`str.replace`, `str.split`) over manual loops when possible.

```python
# Bad
res = ''
for part in pieces:
	res += part

# Good
res = ''.join(pieces)
```

---