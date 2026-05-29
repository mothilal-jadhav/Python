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
| **1st** 🏆 | `()` Parentheses | `(2 + 3) * 4 = 20` | Do what's in parentheses FIRST |
| **2nd** | `**` Exponentiation | `2 ** 3 * 2 = 16` | Power before multiplication |
| **3rd** | `*` `/` `//` `%` | `10 + 2 * 5 = 20` | Multiply/divide before add/subtract |
| **4th** | `+` `-` | `10 + 2 - 3 = 9` | Add/subtract left to right |
| **5th** | Comparisons | `5 > 3 and 2 < 4` | Compare before `and` |
| **6th** | `and` | `True and False or True = True` | `and` before `or` |
| **7th** 🐢 | `or` | (lowest priority) | Do this last |

**Always use parentheses when unsure!** It makes code clear
