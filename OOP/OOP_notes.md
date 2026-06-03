# Object-Oriented Programming (OOP) - Interview Notes

## What is OOP?

OOP stands for **Object-Oriented Programming**. It is a programming style where code is organized using **classes** and **objects**.

- **Class**: blueprint/template
- **Object**: instance of a class
- **Attribute**: data/state
- **Method**: behavior/function inside a class

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        return f"{self.name} scored {self.marks}"

s1 = Student("Amit", 85)
print(s1.display())
```

Interview answer:

> OOP is a programming paradigm based on classes and objects. It combines data and behavior together, making code reusable, modular, maintainable, and scalable.

---

## Four Pillars of OOP

1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

---

## Encapsulation

Encapsulation means binding data and methods together and restricting direct access to internal data.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
```

Interview answer:

> Encapsulation protects object data by hiding internal details and allowing access through controlled methods.

### Access Modifiers in Python

Python does not have strict access modifiers like Java or C++.

- `name`: public
- `_name`: protected by convention
- `__name`: private using name mangling

---

## Abstraction

Abstraction means hiding implementation details and showing only essential features.

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UpiPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using UPI"
```

Interview answer:

> Abstraction hides complex implementation details and exposes only the required interface.

---

## Inheritance

Inheritance allows a child class to reuse properties and methods of a parent class.

```python
class Animal:
    def eat(self):
        return "Eating"

class Dog(Animal):
    def bark(self):
        return "Barking"
```

Interview answer:

> Inheritance allows code reuse by letting one class acquire properties and methods of another class. It represents an `is-a` relationship.

Example:

- Dog is an Animal
- Car is a Vehicle
- Manager is an Employee

---

## Polymorphism

Polymorphism means many forms. The same method name can behave differently for different objects.

```python
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

for animal in [Dog(), Cat()]:
    print(animal.sound())
```

Interview answer:

> Polymorphism allows objects of different classes to be treated through the same interface, while each object provides its own implementation.

---

## Class vs Object

| Class | Object |
|---|---|
| Blueprint/template | Instance of class |
| Logical definition | Runtime entity |
| Does not store object-specific data | Stores actual data |
| Example: `Student` | Example: `s1 = Student()` |

---

## Instance Attribute vs Class Attribute

```python
class Employee:
    company = "Google"  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute
```

Interview answer:

> Instance attributes are unique for each object, while class attributes are shared by all objects of the class.

---

## Instance Method, Class Method, Static Method

```python
class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name

    def show_name(self):
        return self.name

    @classmethod
    def change_company(cls, company):
        cls.company = company

    @staticmethod
    def is_valid_salary(salary):
        return salary > 0
```

Interview answer:

> Instance methods work with object data using `self`. Class methods work with class data using `cls`. Static methods are utility methods that do not need object or class data.

---

## Constructor: `__init__`

`__init__` initializes an object when it is created.

```python
class User:
    def __init__(self, username):
        self.username = username
```

Interview answer:

> `__init__` is the initializer method in Python. It runs automatically when an object is created.

Important:

- `__new__` creates the object.
- `__init__` initializes the object.

---

## `self`

`self` refers to the current object.

```python
class Person:
    def __init__(self, name):
        self.name = name
```

Interview answer:

> `self` represents the current instance of the class and is used to access instance variables and methods.

---

## Method Overriding

Method overriding means a child class provides its own version of a parent method.

```python
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"
```

Interview answer:

> Method overriding happens when a subclass defines a method with the same name as a method in the parent class.

---

## Method Overloading

Python does not support traditional compile-time method overloading.

```python
class Demo:
    def add(self, a, b, c=0):
        return a + b + c
```

Using `*args`:

```python
class Demo:
    def add(self, *args):
        return sum(args)
```

Interview answer:

> Python does not support traditional method overloading like Java. Similar behavior can be achieved using default arguments, `*args`, `**kwargs`, or dispatching.

---

## `super()`

`super()` is used to call parent class methods.

```python
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
```

Interview answer:

> `super()` allows a child class to call methods from its parent class. It is commonly used for constructor chaining.

---

## Duck Typing

Python focuses on behavior, not exact type.

```python
class PdfReport:
    def generate(self):
        return "PDF generated"

class ExcelReport:
    def generate(self):
        return "Excel generated"

def create_report(report):
    return report.generate()
```

Interview answer:

> Duck typing means if an object has the required method or behavior, Python can use it regardless of its actual class.

---

## Operator Overloading

Operator overloading customizes operators for user-defined objects.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```

Interview answer:

> Operator overloading allows custom classes to define behavior for operators like `+`, `==`, and `<` using dunder methods.

---

## Dunder Methods

Dunder methods are special methods with double underscores.

| Method | Purpose |
|---|---|
| `__init__` | Initializes object |
| `__new__` | Creates object |
| `__str__` | User-friendly string |
| `__repr__` | Developer-friendly string |
| `__len__` | Supports `len()` |
| `__eq__` | Supports `==` |
| `__add__` | Supports `+` |
| `__iter__` | Makes object iterable |

---

## `__str__` vs `__repr__`

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Book({self.title!r})"
```

Interview answer:

> `__str__` is for readable user output. `__repr__` is for debugging and developer-friendly output.

---

## `__new__` vs `__init__`

| `__new__` | `__init__` |
|---|---|
| Creates object | Initializes object |
| Called first | Called after `__new__` |
| Returns instance | Returns `None` |
| Rarely used | Commonly used |

Interview answer:

> `__new__` creates an instance, while `__init__` initializes that instance.

---

## MRO

MRO stands for **Method Resolution Order**.

It decides the order in which Python searches for methods in inheritance.

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
```

Interview answer:

> Python uses MRO to resolve method lookup in inheritance, especially multiple inheritance. Python uses C3 linearization.

---

## Diamond Problem

The diamond problem occurs when multiple inheritance creates multiple paths to the same parent class.

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass
```

Interview answer:

> Python solves the diamond problem using MRO, which defines a consistent method lookup order.

---

## Composition

Composition means one class contains another class object.

It represents a `has-a` relationship.

```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()
```

Interview answer:

> Composition is when one object is built using another object. It represents a has-a relationship.

---

## Inheritance vs Composition

| Inheritance | Composition |
|---|---|
| `is-a` relationship | `has-a` relationship |
| Reuses parent behavior | Uses contained object behavior |
| Can create tight coupling | More flexible |
| Dog is an Animal | Car has an Engine |

Interview answer:

> Use inheritance for true `is-a` relationships. Use composition when one object contains or uses another object.

---

## Association, Aggregation, Composition

### Association

General relationship between objects.

Example:

> Teacher teaches Student.

### Aggregation

Weak ownership. Child can exist independently.

Example:

> Department has Teachers.

### Composition

Strong ownership. Child depends on parent.

Example:

> House has Rooms.

Interview answer:

> Association is a general relationship, aggregation is weak ownership, and composition is strong ownership.

---

## Coupling and Cohesion

### Coupling

Coupling means how dependent one class is on another.

Low coupling is good.

### Cohesion

Cohesion means how focused a class is on one responsibility.

High cohesion is good.

Interview answer:

> Good OOP design aims for low coupling and high cohesion.

---

# SOLID Principles

## S - Single Responsibility Principle

A class should have one reason to change.

## O - Open/Closed Principle

Classes should be open for extension but closed for modification.

## L - Liskov Substitution Principle

Child classes should be replaceable wherever parent classes are expected.

## I - Interface Segregation Principle

Do not force classes to implement methods they do not need.

## D - Dependency Inversion Principle

Depend on abstractions, not concrete classes.

Interview answer:

> SOLID principles help create code that is flexible, testable, maintainable, and easy to extend.

---

## Dataclasses

Used for simple data-storing classes.

```python
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
```

Interview answer:

> Dataclasses reduce boilerplate by automatically creating methods like `__init__` and `__repr__`.

---

## Mutable Class Attribute Pitfall

Bad:

```python
class Student:
    subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)
```

Good:

```python
class Student:
    def __init__(self):
        self.subjects = []
```

Interview answer:

> Mutable class attributes are shared by all instances, so changes from one object can affect others.

---

## Shallow Copy vs Deep Copy

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
```

Interview answer:

> A shallow copy copies only the outer object and shares nested objects. A deep copy recursively copies nested objects too.

---

## `is` vs `==`

```python
a = [1, 2]
b = [1, 2]
c = a

print(a == b)  # True
print(a is b)  # False
print(a is c)  # True
```

Interview answer:

> `==` checks value equality. `is` checks object identity, meaning whether two variables refer to the same object.

---

## Interface in Python

Python does not have Java-style interfaces.

Alternatives:

- Abstract base classes
- Protocols
- Duck typing

```python
from typing import Protocol

class Sender(Protocol):
    def send(self, message: str) -> None:
        ...
```

Interview answer:

> Python supports interface-like behavior using abstract base classes, protocols, and duck typing.

---

## Common Design Patterns

### Singleton

Ensures only one object exists.

Use cases:

- Logger
- Configuration
- Database connection manager

### Factory

Creates objects without exposing creation logic.

```python
class PaymentFactory:
    @staticmethod
    def create_payment(method):
        if method == "upi":
            return UpiPayment()
        if method == "card":
            return CardPayment()
        raise ValueError("Invalid method")
```

### Strategy

Allows changing behavior dynamically.

```python
class Cart:
    def __init__(self, discount_strategy):
        self.discount_strategy = discount_strategy

    def final_price(self, amount):
        return self.discount_strategy.calculate(amount)
```

---

## Common Interview Questions

### What are the four pillars of OOP?

Encapsulation, abstraction, inheritance, and polymorphism.

### Class vs Object?

A class is a blueprint. An object is an instance of a class.

### Encapsulation vs Abstraction?

Encapsulation hides data. Abstraction hides implementation details.

### Overloading vs Overriding?

Overloading means same method name with different parameters.  
Overriding means child class redefines parent class method.

### Does Python support multiple inheritance?

Yes. Python supports multiple inheritance and uses MRO to resolve method lookup.

### What is duck typing?

Duck typing means Python focuses on whether an object has required behavior, not its exact class.

### What is MRO?

MRO is Method Resolution Order. It defines the order in which Python searches methods in inheritance.

### What is the diamond problem?

It occurs when multiple inheritance creates multiple paths to the same parent class.

### What is `super()`?

`super()` is used to call parent class methods from a child class.

### What is constructor in Python?

`__init__` is the initializer method called when an object is created.

---

## OOP Design Interview Approach

For system design questions:

1. Identify entities.
2. Create classes.
3. Define attributes.
4. Define methods.
5. Identify relationships.
6. Use inheritance only for `is-a`.
7. Use composition for `has-a`.
8. Keep classes focused.
9. Think about future extension.

Example: Parking Lot

Classes:

- Vehicle
- Car
- Bike
- ParkingSpot
- Ticket
- Payment
- ParkingLot

```python
class Vehicle:
    def __init__(self, number):
        self.number = number

class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def park(self, vehicle):
        if not self.is_available():
            raise ValueError("Spot occupied")
        self.vehicle = vehicle

    def remove_vehicle(self):
        self.vehicle = None
```

---

## Best Practices

- Keep classes small.
- Use meaningful names.
- Avoid deep inheritance.
- Prefer composition when possible.
- Use properties for validation.
- Use dataclasses for simple data.
- Avoid mutable class attributes.
- Keep constructors lightweight.
- Follow SOLID principles.
- Write testable code.

---

## Common Mistakes

- Confusing class and instance attributes.
- Saying Python has strict private variables.
- Overusing inheritance.
- Ignoring MRO.
- Creating unnecessary classes.
- Making one class do too many things.
- Using getters/setters everywhere instead of properties.

---

## Final Interview Summary

OOP is a programming paradigm based on classes and objects. It combines data and behavior into reusable units. The four main pillars are encapsulation, abstraction, inheritance, and polymorphism. OOP helps create modular, reusable, scalable, and maintainable code. In Python, OOP is flexible because of features like duck typing, properties, abstract base classes, dataclasses, and dunder methods.
````