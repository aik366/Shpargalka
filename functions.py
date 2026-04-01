"""
╔══════════════════════════════════════════════════════════════════════╗
║              ШПАРГАЛКА ПО ФУНКЦИЯМ В PYTHON                          ║
║         *args, **kwargs, lambda, декораторы, замыкания               ║
╚══════════════════════════════════════════════════════════════════════╝
"""

print("=" * 70)
print("📚 ШПАРГАЛКА ПО ФУНКЦИЯМ В PYTHON")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. ОПРЕДЕЛЕНИЕ И ВЫЗОВ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. ОПРЕДЕЛЕНИЕ И ВЫЗОВ")
print("─" * 70)


def greet(name):
    """Приветствие пользователя."""
    return f"Привет, {name}!"


print(greet("Алиса"))
print(f"Docstring: {greet.__doc__}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. ПАРАМЕТРЫ ПО УМОЛЧАНИЮ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. ПАРАМЕТРЫ ПО УМОЛЧАНИЮ")
print("─" * 70)


def power(base, exp=2):
    return base**exp


print(f"\npower(3):     {power(3)}")
print(f"power(3, 3):  {power(3, 3)}")


# ⚠️ Опасность изменяемых значений по умолчанию
def bad_append(item, lst=[]):
    lst.append(item)
    return lst


def good_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


print(f"\nbad_append(1): {bad_append(1)}")
print(f"bad_append(2): {bad_append(2)}  # ← баг!")
print(f"good_append(1): {good_append(1)}")
print(f"good_append(2): {good_append(2)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. *args — произвольное число позиционных аргументов
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. *args")
print("─" * 70)


def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)


print(f"\naverage(1, 2, 3):     {average(1, 2, 3)}")
print(f"average(10, 20):      {average(10, 20)}")
print(f"average(5):           {average(5)}")


def concat(separator, *args):
    return separator.join(str(a) for a in args)


print(f"\nconcat('-', 1, 2, 3): {concat('-', 1, 2, 3)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. **kwargs — произвольное число именованных аргументов
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. **kwargs")
print("─" * 70)


def create_user(**kwargs):
    return kwargs


user = create_user(name="Алиса", age=30, city="Москва")
print(f"\ncreate_user: {user}")


def print_config(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


print("\nКонфигурация:")
print_config(host="localhost", port=8080, debug=True)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. *args + **kwargs вместе
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. *args + **kwargs")
print("─" * 70)


def full_signature(*args, **kwargs):
    print(f"  args:   {args}")
    print(f"  kwargs: {kwargs}")


print("\nfull_signature(1, 2, 3, name='Bob', age=25):")
full_signature(1, 2, 3, name="Bob", age=25)


# Порядок параметров: positional, *args, keyword-only, **kwargs
def order(a, b, *args, c=10, **kwargs):
    print(f"  a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}")


print("\norder(1, 2, 3, 4, c=20, d=30):")
order(1, 2, 3, 4, c=20, d=30)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. KEYWORD-ONLY АРГУМЕНТЫ (Python 3+)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. KEYWORD-ONLY АРГУМЕНТЫ")
print("─" * 70)


def greet_formal(name, *, formal=False):
    if formal:
        return f"Уважаемый(ая) {name}!"
    return f"Привет, {name}!"


print(f"\ngreet_formal('Алиса'): {greet_formal('Алиса')}")
print(f"greet_formal('Алиса', formal=True): {greet_formal('Алиса', formal=True)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. LAMBDA-ФУНКЦИИ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. LAMBDA-ФУНКЦИИ")
print("─" * 70)

# Базовый синтаксис: lambda аргументы: выражение
add = lambda x, y: x + y
print(f"\nadd(3, 5): {add(3, 5)}")

square = lambda x: x**2
print(f"square(7): {square(7)}")

# Сортировка по ключу
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
by_name = sorted(students, key=lambda x: x[0])
by_score = sorted(students, key=lambda x: x[1], reverse=True)

print(f"\nПо имени: {by_name}")
print(f"По баллу: {by_score}")

# Фильтрация
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"\nЧётные: {evens}")

# map
squared = list(map(lambda x: x**2, nums[:5]))
print(f"Квадраты: {squared}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. ЗАМЫКАНИЯ (CLOSURES)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. ЗАМЫКАНИЯ")
print("─" * 70)


def multiplier(n):
    return lambda x: x * n


double = multiplier(2)
triple = multiplier(3)

print(f"\ndouble(5): {double(5)}")
print(f"triple(5): {triple(5)}")


# Фабрика функций
def make_greeting(language):
    greetings = {
        "en": lambda name: f"Hello, {name}!",
        "ru": lambda name: f"Привет, {name}!",
        "es": lambda name: f"¡Hola, {name}!",
    }
    return greetings.get(language, greetings["en"])


greet_ru = make_greeting("ru")
greet_es = make_greeting("es")
print(f"\ngreet_ru('Алиса'): {greet_ru('Алиса')}")
print(f"greet_es('Алиса'): {greet_es('Алиса')}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 9. ОБЛАСТЬ ВИДИМОСТИ (SCOPE)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 9. ОБЛАСТЬ ВИДИМОСТИ (LEGB)")
print("─" * 70)

print("""
LEGB Rule:
  L — Local (внутри функции)
  E — Enclosing (во внешней функции)
  G — Global (на уровне модуля)
  B — Built-in (встроенные: len, print, etc.)
""")

x = "global"


def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(f"  inner: {x}")

    inner()
    print(f"  outer: {x}")


print("Вызов outer():")
outer()
print(f"Глобальная: {x}")

# global и nonlocal
counter = 0


def increment():
    global counter
    counter += 1


increment()
increment()
print(f"\nГлобальный counter: {counter}")


def make_counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


c = make_counter()
print(f"nonlocal counter: {c()}, {c()}, {c()}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 10. АННОТАЦИИ ТИПОВ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 10. АННОТАЦИИ ТИПОВ")
print("─" * 70)


def add(a: int, b: int) -> int:
    return a + b


def greet_user(name: str, age: int = 0) -> str:
    return f"{name}, {age} лет"


from typing import List, Dict, Optional, Union


def process_data(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}


def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)


print(f"\nadd(3, 5): {add(3, 5)}")
print(f"greet_user('Алиса', 30): {greet_user('Алиса', 30)}")
print(f"process_data(['hi', 'hello']): {process_data(['hi', 'hello'])}")
print(f"find_user(1): {find_user(1)}")
print(f"find_user(99): {find_user(99)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 11. ПОЛЕЗНЫЕ ПРИЁМЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 11. ПОЛЕЗНЫЕ ПРИЁМЫ")
print("─" * 70)


# Распаковка аргументов
def add3(a, b, c):
    return a + b + c


args = [1, 2, 3]
kwargs = {"a": 10, "b": 20, "c": 30}
print(f"\nadd3(*args): {add3(*args)}")
print(f"add3(**kwargs): {add3(**kwargs)}")


# Функция как аргумент
def apply(func, value):
    return func(value)


print(f"\napply(lambda x: x*2, 5): {apply(lambda x: x * 2, 5)}")


# Рекурсия
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


print(f"\nfactorial(5): {factorial(5)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# ОПРЕДЕЛЕНИЕ
def func(a, b, c=10, *args, d=20, **kwargs):
    pass

# LAMBDA
lambda x, y: x + y
sorted(data, key=lambda x: x[1])
list(filter(lambda x: x > 0, nums))

# *args — кортеж позиционных аргументов
# **kwargs — словарь именованных аргументов

# РАСПАКОВКА
func(*[1, 2, 3])      # func(1, 2, 3)
func(**{"a": 1})      # func(a=1)

# ЗАМЫКАНИЕ
def outer(x):
    def inner(y):
        return x + y
    return inner

# ТИПИЗАЦИЯ
def func(a: int, b: str = "hi") -> bool:
    return True
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
