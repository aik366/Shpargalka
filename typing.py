"""
╔══════════════════════════════════════════════════════════════════════╗
║            ШПАРГАЛКА ПО ТИПИЗАЦИИ В PYTHON                           ║
║        typing, TypeVar, Protocol, Union, Optional и др.              ║
╚══════════════════════════════════════════════════════════════════════╝
"""

from typing import (
    List,
    Dict,
    Set,
    Tuple,
    Optional,
    Union,
    Any,
    Callable,
    TypeVar,
    Generic,
    Protocol,
    Literal,
    Final,
    TypedDict,
    NamedTuple,
)

print("=" * 70)
print("📚 ШПАРГАЛКА ПО ТИПИЗАЦИИ В PYTHON")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. БАЗОВЫЕ АННОТАЦИИ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. БАЗОВЫЕ АННОТАЦИИ")
print("─" * 70)


def greet(name: str) -> str:
    return f"Привет, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def is_positive(n: float) -> bool:
    return n > 0


def nothing() -> None:
    pass


print(f"greet('Алиса'): {greet('Алиса')}")
print(f"add(3, 5): {add(3, 5)}")
print(f"is_positive(3.14): {is_positive(3.14)}")

# Переменные
name: str = "Алиса"
age: int = 30
height: float = 1.68
active: bool = True

print(f"\n{name}, {age} лет, рост {height}м, активен: {active}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. КОЛЛЕКЦИИ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. КОЛЛЕКЦИИ")
print("─" * 70)

# Python 3.9+ можно использовать встроенные типы
# Для совместимости используем typing

numbers: List[int] = [1, 2, 3, 4, 5]
mapping: Dict[str, int] = {"a": 1, "b": 2}
unique: Set[int] = {1, 2, 3}
pair: Tuple[str, int] = ("age", 30)

print(f"List[int]: {numbers}")
print(f"Dict[str, int]: {mapping}")
print(f"Set[int]: {unique}")
print(f"Tuple[str, int]: {pair}")


# Python 3.9+ синтаксис (рекомендуемый)
def process(items: list[int]) -> dict[str, int]:
    return {item: len(item) for item in items if isinstance(item, str)}


print(f"\nprocess(['hi', 'hello']): {process(['hi', 'hello'])}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. OPTIONAL И UNION
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. OPTIONAL И UNION")
print("─" * 70)


# Optional[X] == Union[X, None]
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)


print(f"\nfind_user(1): {find_user(1)}")
print(f"find_user(99): {find_user(99)}")


# Union — несколько типов
def parse(value: Union[str, int, float]) -> float:
    return float(value)


print(f"\nparse('3.14'): {parse('3.14')}")
print(f"parse(42): {parse(42)}")


# Python 3.10+ синтаксис с |
def double(x: int | float) -> int | float:
    return x * 2


print(f"\ndouble(5): {double(5)}")
print(f"double(3.14): {double(3.14)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. ANY
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. ANY")
print("─" * 70)


def process_any(data: Any) -> str:
    return str(data)


print(f"\nprocess_any(42): {process_any(42)}")
print(f"process_any('hello'): {process_any('hello')}")
print(f"process_any([1,2,3]): {process_any([1, 2, 3])}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. CALLABLE
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. CALLABLE")
print("─" * 70)


def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)


def multiply(x: int, y: int) -> int:
    return x * y


print(f"\napply(multiply, 3, 5): {apply(multiply, 3, 5)}")
print(f"apply(lambda x, y: x + y, 3, 5): {apply(lambda x, y: x + y, 3, 5)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. TYPEVAR И GENERIC
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. TYPEVAR И GENERIC")
print("─" * 70)

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


print(f"\nfirst([1, 2, 3]): {first([1, 2, 3])}")
print(f"first(['a', 'b']): {first(['a', 'b'])}")


# Generic класс
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def is_empty(self) -> bool:
        return len(self._items) == 0


int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(f"\nStack[int].pop(): {int_stack.pop()}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. PROTOCOL (Structural Subtyping)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. PROTOCOL")
print("─" * 70)


class Quackable(Protocol):
    def quack(self) -> str: ...


class Duck:
    def quack(self) -> str:
        return "Кря!"


class Person:
    def quack(self) -> str:
        return "Я притворяюсь уткой!"


def make_quack(obj: Quackable) -> str:
    return obj.quack()


duck = Duck()
person = Person()

print(f"\nmake_quack(duck): {make_quack(duck)}")
print(f"make_quack(person): {make_quack(person)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. LITERAL
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. LITERAL")
print("─" * 70)


def set_mode(mode: Literal["read", "write", "append"]) -> str:
    return f"Режим: {mode}"


print(f"\nset_mode('read'): {set_mode('read')}")
print(f"set_mode('write'): {set_mode('write')}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 9. TYPEDDICT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 9. TYPEDDICT")
print("─" * 70)


class User(TypedDict):
    name: str
    age: int
    email: Optional[str]


user: User = {
    "name": "Алиса",
    "age": 30,
    "email": "alice@example.com",
}

print(f"\nUser: {user}")
print(f"user['name']: {user['name']}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 10. NAMEDTUPLE
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 10. NAMEDTUPLE")
print("─" * 70)


class Point(NamedTuple):
    x: float
    y: float


p = Point(3.0, 4.0)
print(f"\nPoint: {p}")
print(f"p.x: {p.x}, p.y: {p.y}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 11. FINAL
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 11. FINAL")
print("─" * 70)

MAX_SIZE: Final = 100
print(f"\nMAX_SIZE: {MAX_SIZE}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# БАЗОВЫЕ
def func(a: int, b: str) -> bool: ...

# КОЛЛЕКЦИИ (Python 3.9+)
list[int], dict[str, int], set[int], tuple[str, int]

# OPTIONAL / UNION
Optional[str]       # str или None
Union[str, int]     # str или int
str | int           # Python 3.10+

# SPECIAL
Any                 # Любой тип
Callable[[int], str]# Функция
Literal["a", "b"]   # Конкретные значения
Final               # Константа

# GENERIC
T = TypeVar("T")
class Stack(Generic[T]): ...

# PROTOCOL
class Quackable(Protocol):
    def quack(self) -> str: ...

# TYPEDDICT
class User(TypedDict):
    name: str
    age: int
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
