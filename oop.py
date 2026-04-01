"""
╔══════════════════════════════════════════════════════════════════════╗
║              ШПАРГАЛКА ПО ООП В PYTHON                               ║
║         Классы, наследование, магические методы, property            ║
╚══════════════════════════════════════════════════════════════════════╝
"""

print("=" * 70)
print("📚 ШПАРГАЛКА ПО ООП В PYTHON")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. БАЗОВЫЙ КЛАСС
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. БАЗОВЫЙ КЛАСС")
print("─" * 70)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Привет, я {self.name}, мне {self.age} лет"

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"


p = Person("Алиса", 30)
print(f"\np: {p}")
print(f"p.greet(): {p.greet()}")
print(f"repr(p): {repr(p)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. АТРИБУТЫ КЛАССА И ЭКЗЕМПЛЯРА
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. АТРИБУТЫ КЛАССА И ЭКЗЕМПЛЯРА")
print("─" * 70)


class Employee:
    company = "TechCorp"  # Атрибут класса (общий для всех)
    employee_count = 0  # Счётчик

    def __init__(self, name, salary):
        self.name = name  # Атрибут экземпляра
        self.salary = salary
        Employee.employee_count += 1

    def info(self):
        return f"{self.name} работает в {self.company}"


e1 = Employee("Алиса", 100000)
e2 = Employee("Боб", 120000)

print(f"\ne1.company: {e1.company}")
print(f"e2.company: {e2.company}")
print(f"Сотрудников: {Employee.employee_count}")
print(f"e1.info(): {e1.info()}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. НАСЛЕДОВАНИЕ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. НАСЛЕДОВАНИЕ")
print("─" * 70)


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name}: {self.sound}!"

    def __str__(self):
        return f"Animal({self.name})"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Гав")
        self.breed = breed

    def fetch(self):
        return f"{self.name} ({self.breed}) принёс мяч!"


class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Мяу")
        self.indoor = indoor


dog = Dog("Бобик", "Лабрадор")
cat = Cat("Мурка")

print(f"\ndog.speak(): {dog.speak()}")
print(f"dog.fetch(): {dog.fetch()}")
print(f"cat.speak(): {cat.speak()}")

# Проверка наследования
print(f"\nisinstance(dog, Dog): {isinstance(dog, Dog)}")
print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ")
print("─" * 70)


class Flyable:
    def fly(self):
        return "Лечу!"


class Swimmable:
    def swim(self):
        return "Плыву!"


class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name


duck = Duck("Дональд")
print(f"\n{duck.name}: {duck.fly()}, {duck.swim()}")
print(f"MRO: {Duck.__mro__}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. PROPERTY (СВОЙСТВА)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. PROPERTY")
print("─" * 70)


class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Температура ниже абсолютного нуля!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9


t = Temperature(25)
print(f"\nt.celsius: {t.celsius}")
print(f"t.fahrenheit: {t.fahrenheit}")

t.fahrenheit = 212
print(f"После t.fahrenheit = 212:")
print(f"  t.celsius: {t.celsius}")
print(f"  t.fahrenheit: {t.fahrenheit}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. МАГИЧЕСКИЕ МЕТОДЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. МАГИЧЕСКИЕ МЕТОДЫ")
print("─" * 70)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __len__(self):
        return 2  # 2D вектор


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"\nv1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 3: {v1 * 3}")
print(f"v1 == v2: {v1 == v2}")
print(f"abs(v1): {abs(v1):.2f}")
print(f"bool(v1): {bool(v1)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. КЛАСС-МЕТОДЫ И СТАТИЧЕСКИЕ МЕТОДЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. КЛАСС-МЕТОДЫ И СТАТИЧЕСКИЕ МЕТОДЫ")
print("─" * 70)


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

    @classmethod
    def from_string(cls, date_str):
        """Создание из строки 'ДД.ММ.ГГГГ'."""
        day, month, year = map(int, date_str.split("."))
        return cls(year, month, day)

    @classmethod
    def today(cls):
        """Создание с сегодняшней датой."""
        from datetime import date

        today = date.today()
        return cls(today.year, today.month, today.day)

    @staticmethod
    def is_leap_year(year):
        """Проверка високосного года."""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


d1 = Date.from_string("25.12.2026")
d2 = Date.today()

print(f"\nfrom_string: {d1}")
print(f"today: {d2}")
print(f"is_leap_year(2024): {Date.is_leap_year(2024)}")
print(f"is_leap_year(2025): {Date.is_leap_year(2025)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. ИНКАПСУЛЯЦИЯ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. ИНКАПСУЛЯЦИЯ")
print("─" * 70)


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # Публичный
        self._balance = balance  # Защищённый (convention)
        self.__pin = "1234"  # Приватный (name mangling)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    @property
    def balance(self):
        return self._balance


account = BankAccount("Алиса", 1000)
print(f"\naccount.owner: {account.owner}")
print(f"account.balance: {account.balance}")
print(f"account.deposit(500): {account.deposit(500)}")
print(f"account.balance: {account.balance}")
print(f"account.withdraw(200): {account.withdraw(200)}")
print(f"account.balance: {account.balance}")

# Доступ к приватному атрибуту (name mangling)
print(f"account._BankAccount__pin: {account._BankAccount__pin}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 9. АБСТРАКТНЫЕ КЛАССЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 9. АБСТРАКТНЫЕ КЛАССЫ")
print("─" * 70)

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math

        return math.pi * self.radius**2

    def perimeter(self):
        import math

        return 2 * math.pi * self.radius


rect = Rectangle(5, 3)
circle = Circle(4)

print(f"\n{rect}: area={rect.area()}, perimeter={rect.perimeter()}")
print(f"{circle}: area={circle.area():.2f}, perimeter={circle.perimeter():.2f}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 10. DATA CLASSES (Python 3.7+)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 10. DATA CLASSES")
print("─" * 70)

from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    @property
    def total(self):
        return self.price * self.quantity


@dataclass(order=True)
class Student:
    grade: float
    name: str = field(compare=False)


p = Product("Ноутбук", 75000, 2)
print(f"\nProduct: {p}")
print(f"Total: {p.total}")

students = [Student(85.5, "Алиса"), Student(92.0, "Боб"), Student(78.0, "Чарли")]
print(f"Sorted by grade: {sorted(students)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# КЛАСС
class MyClass:
    def __init__(self, x):
        self.x = x

    def method(self):
        return self.x

# НАСЛЕДОВАНИЕ
class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

# PROPERTY
@property
def x(self):
    return self._x

@x.setter
def x(self, value):
    self._x = value

# КЛАСС/СТАТИК МЕТОДЫ
@classmethod
def from_str(cls, s): ...

@staticmethod
def utility(): ...

# МАГИЧЕСКИЕ МЕТОДЫ
__str__    # str(obj)
__repr__   # repr(obj)
__eq__     # obj1 == obj2
__add__    # obj1 + obj2
__len__    # len(obj)
__getitem__# obj[key]
__iter__   # for x in obj
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
