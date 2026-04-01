"""
╔══════════════════════════════════════════════════════════════════════╗
║         ШПАРГАЛКА ПО DATACLASSES В PYTHON                            ║
║        @dataclass, field, frozen, Post-init и др.                    ║
╚══════════════════════════════════════════════════════════════════════╝
"""

from dataclasses import dataclass, field, asdict, astuple, replace, fields
from typing import List, Optional

print("=" * 70)
print("📚 ШПАРГАЛКА ПО DATACLASSES")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. БАЗОВЫЙ DATACLASS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. БАЗОВЫЙ DATACLASS")
print("─" * 70)


@dataclass
class Point:
    x: float
    y: float


p = Point(3.0, 4.0)
print(f"\nPoint: {p}")
print(f"p.x: {p.x}, p.y: {p.y}")

# Автоматически генерируются:
# __init__, __repr__, __eq__

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ")
print("─" * 70)


@dataclass
class User:
    name: str
    age: int = 0
    active: bool = True


u1 = User("Алиса", 30)
u2 = User("Боб")
u3 = User("Чарли", 25, False)

print(f"\nu1: {u1}")
print(f"u2: {u2}")
print(f"u3: {u3}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. FIELD — ТОНКАЯ НАСТРОЙКА
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. FIELD")
print("─" * 70)


@dataclass
class Product:
    name: str
    price: float
    quantity: int = field(default=0)
    tags: List[str] = field(default_factory=list)
    _id: int = field(default=0, repr=False)


p1 = Product("Ноутбук", 75000)
p2 = Product("Телефон", 50000, 5, ["sale", "new"], 42)

print(f"\np1: {p1}")
print(f"p2: {p2}")
print(f"p2.tags: {p2.tags}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. INIT=False И POST-INIT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. POST-INIT")
print("─" * 70)


@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = self.width * self.height


rect = Rectangle(5, 3)
print(f"\nRectangle: {rect}")
print(f"rect.area: {rect.area}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. FROZEN (НЕИЗМЕНЯЕМЫЙ)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. FROZEN")
print("─" * 70)


@dataclass(frozen=True)
class ImmutablePoint:
    x: float
    y: float


p = ImmutablePoint(3.0, 4.0)
print(f"\nImmutablePoint: {p}")

try:
    p.x = 10.0
except Exception as e:
    print(f"Ошибка при изменении: {type(e).__name__}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. ORDER И SORTING
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. ORDER И SORTING")
print("─" * 70)


@dataclass(order=True)
class Student:
    grade: float
    name: str = field(compare=False)


students = [
    Student(85.5, "Алиса"),
    Student(92.0, "Боб"),
    Student(78.0, "Чарли"),
    Student(92.0, "Дейв"),
]

print("\nСортировка по grade:")
for s in sorted(students):
    print(f"  {s}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. ПОЛЕЗНЫЕ ФУНКЦИИ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. ПОЛЕЗНЫЕ ФУНКЦИИ")
print("─" * 70)


@dataclass
class Person:
    name: str
    age: int
    city: str = "Москва"


person = Person("Алиса", 30)

# asdict — в словарь
d = asdict(person)
print(f"\nasdict: {d}")

# astuple — в кортеж
t = astuple(person)
print(f"astuple: {t}")

# replace — копирование с изменением
person2 = replace(person, age=31, city="Питер")
print(f"replace: {person2}")

# fields — информация о полях
print(f"\nfields:")
for f in fields(person):
    print(f"  {f.name}: {f.type}, default={f.default}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. НАСЛЕДОВАНИЕ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. НАСЛЕДОВАНИЕ")
print("─" * 70)


@dataclass
class Animal:
    name: str
    sound: str


@dataclass
class Dog(Animal):
    breed: str
    tricks: List[str] = field(default_factory=list)


dog = Dog("Бобик", "Гав", "Лабрадор", ["Сидеть", "Лежать"])
print(f"\nDog: {dog}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 9. KW_ONLY (Python 3.10+)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 9. KW_ONLY (Python 3.10+)")
print("─" * 70)

print("""
from dataclasses import dataclass, KW_ONLY

@dataclass
class Config:
    host: str
    port: int
    _: KW_ONLY
    debug: bool = False
    timeout: float = 5.0

# host и port — позиционные
# debug и timeout — только ключевые
cfg = Config("localhost", 8080, debug=True)
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 10. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 10. ПРАКТИЧЕСКИЕ ПРИМЕРЫ")
print("─" * 70)


# 1. API Response
@dataclass
class APIResponse:
    status: int
    data: dict
    message: str = ""

    @property
    def is_success(self):
        return 200 <= self.status < 300


resp = APIResponse(200, {"id": 1, "name": "Alice"})
print(f"\nAPIResponse: {resp}")
print(f"is_success: {resp.is_success}")


# 2. Конфигурация
@dataclass(frozen=True)
class DBConfig:
    host: str
    port: int = 5432
    database: str = "mydb"
    user: str = "admin"
    password: str = field(default="", repr=False)

    @property
    def connection_string(self):
        return f"postgresql://{self.user}@{self.host}:{self.port}/{self.database}"


db = DBConfig("localhost")
print(f"\nDBConfig: {db}")
print(f"connection_string: {db.connection_string}")


# 3. JSON сериализация
@dataclass
class Order:
    id: int
    items: List[str]
    total: float


order = Order(1, ["Товар 1", "Товар 2"], 1500.0)
import json

json_str = json.dumps(asdict(order), indent=2, ensure_ascii=False)
print(f"\nJSON:\n{json_str}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# БАЗОВЫЙ
@dataclass
class Point:
    x: float
    y: float

# ПАРАМЕТРЫ DATACLASS
@dataclass(frozen=True, order=True, repr=True, eq=True)

# FIELD
field(default=0)
field(default_factory=list)
field(repr=False)
field(compare=False)
field(init=False)

# POST-INIT
def __post_init__(self):
    self.computed = self.x * self.y

# ФУНКЦИИ
asdict(obj)       # → dict
astuple(obj)      # → tuple
replace(obj, x=10) # Копия с изменением
fields(obj)       # Информация о полях

# PYTHON 3.10+
_: KW_ONLY
debug: bool = False  # Только ключевой аргумент
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
