"""
╔══════════════════════════════════════════════════════════════════════╗
║            ШПАРГАЛКА ПО ДЕКОРАТОРАМ В PYTHON                         ║
║        Основы, декораторы с параметрами, functools                   ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import time
import functools

print("=" * 70)
print("📚 ШПАРГАЛКА ПО ДЕКОРАТОРАМ")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. ОСНОВЫ — ФУНКЦИИ КАК ОБЪЕКТЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. ФУНКЦИИ КАК ОБЪЕКТЫ")
print("─" * 70)


def greet(name):
    return f"Привет, {name}!"


# Присваивание
say_hello = greet
print(f"\nsay_hello('Алиса'): {say_hello('Алиса')}")


# Передача как аргумент
def call(func, arg):
    return func(arg)


print(f"call(greet, 'Боб'): {call(greet, 'Боб')}")


# Возврат функции
def make_greeting(prefix):
    def inner(name):
        return f"{prefix}, {name}!"

    return inner


formal = make_greeting("Уважаемый")
print(f"formal('Иван'): {formal('Иван')}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. ПРОСТОЙ ДЕКОРАТОР
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. ПРОСТОЙ ДЕКОРАТОР")
print("─" * 70)


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  Вызов {func.__name__}()")
        result = func(*args, **kwargs)
        print(f"  Результат: {result}")
        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


result = add(3, 5)
print(f"add.__name__: {add.__name__}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. ДЕКОРАТОР ЗАМЕРА ВРЕМЕНИ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. ДЕКОРАТОР ЗАМЕРА ВРЕМЕНИ")
print("─" * 70)


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__}() выполнилась за {elapsed:.4f} сек")
        return result

    return wrapper


@timer
def slow_function(n):
    time.sleep(0.1)
    return sum(range(n))


result = slow_function(1000000)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. ДЕКОРАТОР КЭШИРОВАНИЯ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. ДЕКОРАТОР КЭШИРОВАНИЯ")
print("─" * 70)


def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"\nfibonacci(30): {fibonacci(30)}")
print(f"fibonacci(30) (из кэша): {fibonacci(30)}")


# Встроенный lru_cache
@functools.lru_cache(maxsize=128)
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


print(f"\nfib_cached(30): {fib_cached(30)}")
print(f"cache_info: {fib_cached.cache_info()}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. ДЕКОРАТОР С ПАРАМЕТРАМИ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. ДЕКОРАТОР С ПАРАМЕТРАМИ")
print("─" * 70)


def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f"  Привет, {name}!")


greet("Алиса")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. ДЕКОРАТОР ПРОВЕРКИ ТИПОВ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. ДЕКОРАТОР ПРОВЕРКИ ТИПОВ")
print("─" * 70)


def type_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        hints = func.__annotations__
        for name, value in zip(func.__code__.co_varnames, args):
            if name in hints and not isinstance(value, hints[name]):
                raise TypeError(
                    f"Аргумент '{name}' должен быть {hints[name].__name__}, "
                    f"получен {type(value).__name__}"
                )
        return func(*args, **kwargs)

    return wrapper


@type_check
def multiply(a: int, b: int) -> int:
    return a * b


print(f"\nmultiply(3, 5): {multiply(3, 5)}")

try:
    multiply("3", 5)
except TypeError as e:
    print(f"multiply('3', 5): {e}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. ДЕКОРАТОР retry
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. ДЕКОРАТОР RETRY")
print("─" * 70)


def retry(max_attempts=3, delay=0.1, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts:
                        raise
                    print(f"  Попытка {attempt}/{max_attempts}: {e}")
                    time.sleep(delay)

        return wrapper

    return decorator


call_count = 0


@retry(max_attempts=3, delay=0.05)
def unstable():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError("Нет соединения")
    return "Успех!"


result = unstable()
print(f"\nРезультат: {result}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. НЕСКОЛЬКО ДЕКОРАТОРОВ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. НЕСКОЛЬКО ДЕКОРАТОРОВ")
print("─" * 70)


def decorator_a(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("  A — до")
        result = func(*args, **kwargs)
        print("  A — после")
        return result

    return wrapper


def decorator_b(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("  B — до")
        result = func(*args, **kwargs)
        print("  B — после")
        return result

    return wrapper


@decorator_a
@decorator_b
def hello():
    print("  hello!")


print("\nПорядок выполнения:")
hello()

# ═══════════════════════════════════════════════════════════════════════
# 🔹 9. ДЕКОРАТОР КЛАССА
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 9. ДЕКОРАТОР КЛАССА")
print("─" * 70)


def add_repr(cls):
    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{cls.__name__}({attrs})"

    cls.__repr__ = __repr__
    return cls


@add_repr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(3, 4)
print(f"\n{p}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 10. ВСТРОЕННЫЕ ДЕКОРАТОРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 10. ВСТРОЕННЫЕ ДЕКОРАТОРЫ")
print("─" * 70)


class Example:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @staticmethod
    def utility():
        return "Статический метод"

    @classmethod
    def from_string(cls, s):
        return cls(int(s))


e = Example(42)
print(f"\n@property: {e.value}")
e.value = 100
print(f"@property setter: {e.value}")
print(f"@staticmethod: {Example.utility()}")
print(f"@classmethod: {Example.from_string('99').value}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# ПРОСТОЙ ДЕКОРАТОР
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # до
        result = func(*args, **kwargs)
        # после
        return result
    return wrapper

# С ПАРАМЕТРАМИ
def decorator(arg):
    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return inner

# functools.wraps — сохраняет имя и docstring
# functools.lru_cache — кэширование
# @property, @staticmethod, @classmethod — встроенные
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
