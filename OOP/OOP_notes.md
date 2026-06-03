# Object-Oriented Programming (OOP)

Object-oriented programming is a way to organize code around objects and classes. In Python, OOP is often used for modeling real-world entities, organizing systems, and improving code reusability.

---

## Key concepts

- **Class**: a template for objects, defining attributes and behavior.
- **Object / instance**: a runtime entity created from a class.
- **Encapsulation**: bundling data and methods, controlling access.
- **Inheritance**: deriving a new class from an existing class.
- **Polymorphism**: using the same interface for different implementations.
- **Abstraction**: exposing only relevant behavior and hiding implementation details.

---

## Python class basics

```python
class Animal:
    species = 'Unknown'  # class attribute

    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound"

    def describe(self):
        return f"{self.name} is {self.age} years old"

cat = Animal('Milo', 2)
print(cat.describe())
print(cat.speak())
```

- `__init__` is the constructor for initializing new instances.
- `self` refers to the instance.
- Class attributes are shared by all instances, instance attributes are unique per object.

---

## Encapsulation and access control

Python does not enforce access modifiers, but naming conventions signal intent:

- Public: `self.value`
- Protected (by convention): `self._value`
- Private name-mangled: `self.__value`

```python
class Account:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError('Insufficient funds')
        self._balance -= amount
```

Use properties for controlled access:

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError('Name cannot be empty')
        self._name = value
```

---

## Inheritance

Inheritance lets a subclass extend or override behavior from a base class.

```python
class Dog(Animal):
    species = 'Canine'

    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    species = 'Feline'

    def speak(self):
        return f"{self.name} meows"

animals = [Dog('Rex', 4), Cat('Luna', 3)]
for animal in animals:
    print(animal.speak())
```

- Use `super()` to call the parent class implementation.
- Inheritance supports code reuse but should not be overused.

```python
class Employee(Person):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role
```

---

## Polymorphism

Polymorphism means different objects respond to the same method call in their own way.

```python
for animal in animals:
    print(animal.speak())
```

This works because each subclass implements `speak()`.

Duck typing focuses on available methods rather than explicit types.

```python
class Car:
    def drive(self):
        return 'Car is driving'

class Bike:
    def drive(self):
        return 'Bike is driving'

def start(vehicle):
    print(vehicle.drive())
```

---

## Abstraction

Abstraction means presenting a simple interface and hiding details.

- Abstract base classes (ABCs) help define required interfaces.
- Use `abc.ABC` and `@abstractmethod` for formal contracts.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

---

## Special methods / dunder methods

Special methods customize Python behavior.

- `__repr__` / `__str__`
- `__eq__`, `__lt__`, `__hash__`
- `__len__`, `__iter__`, `__getitem__`
- `__enter__`, `__exit__`

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
```

---

## Class methods and static methods

- `@staticmethod` — function inside class namespace without instance access
- `@classmethod` — receives class itself as first argument

```python
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def validate(value):
        return value >= 0
```

Use class methods for alternative constructors and static methods for utility functions related to the class.

---

## Composition vs inheritance

Prefer composition when objects should collaborate rather than share an ``is-a`` relationship.

```python
class Engine:
    def start(self):
        return 'Engine started'

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()
```

If a class can be modeled with another object as a component, composition is often safer and more flexible than deep inheritance hierarchies.

---

## Method resolution order (MRO)

Python uses C3 linearization for multiple inheritance.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
print(D.mro())
```

Know how `super()` works in diamond-shaped hierarchies to avoid duplicate initialization.

---

## Common interview topics

- Difference between class and instance attributes
- Method resolution order and `super()`
- `__init__` vs `__new__`
- Mutable vs immutable objects in classes
- Encapsulation and how Python handles it
- Composition vs inheritance
- Polymorphism and duck typing
- When to use abstract base classes
- Data hiding using naming conventions and properties
- SOLID principles at a high level

---

## SOLID principles (Python-friendly summary)

- **Single Responsibility**: one class should have one reason to change.
- **Open/Closed**: classes should be open for extension, closed for modification.
- **Liskov Substitution**: subclasses should be replaceable with their base classes.
- **Interface Segregation**: prefer small, focused interfaces.
- **Dependency Inversion**: depend on abstractions, not concrete classes.

---

## Best practices for Python OOP

- Favor simple classes and small methods.
- Use `@property` for attribute access logic instead of public getters/setters.
- Avoid unnecessary inheritance; prefer composition and interfaces.
- Keep class responsibilities narrow.
- Use dataclasses for immutable or plain data containers.
- Use type hints and docstrings for clarity.

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
```

---

## Common pitfalls

- Overusing inheritance and creating deep class hierarchies.
- Mutating class attributes unintentionally.
- Relying on private names instead of clear interfaces.
- Ignoring Pythonic duck typing and strict interface enforcement.
- Implementing too much logic inside `__init__`.

---

## Practical example

```python
class Repository(ABC):
    @abstractmethod
    def save(self, item):
        pass

class InMemoryRepository(Repository):
    def __init__(self):
        self._items = []

    def save(self, item):
        self._items.append(item)
        return item
```

This example shows abstraction, interface design, and a concrete implementation.

---

## Quick reference

- Define class: `class Name:`
- Create instance: `obj = Name()`
- Constructor: `def __init__(self, ...):`
- Inheritance: `class Sub(Base):`
- Call parent: `super().__init__(...)`
- Private naming: `_protected`, `__private`
- Special methods: `__repr__`, `__eq__`, `__add__`
- Property: `@property`
- Abstract method: `@abstractmethod`

End of OOP notes.
