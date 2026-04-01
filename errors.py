"""
╔══════════════════════════════════════════════════════════════════════╗
║          ШПАРГАЛКА ПО ОБРАБОТКЕ ОШИБОК В PYTHON                      ║
║         try/except/finally/else, исключения, кастомные ошибки        ║
╚══════════════════════════════════════════════════════════════════════╝
"""

print("=" * 70)
print("📚 ШПАРГАЛКА ПО ОБРАБОТКЕ ОШИБОК")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. БАЗОВЫЙ TRY/EXCEPT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. БАЗОВЫЙ TRY/EXCEPT")
print("─" * 70)

# Простой пример
try:
    result = 10 / 0
except ZeroDivisionError:
    print("\nДеление на ноль!")

# С переменной исключения
try:
    int("не число")
except ValueError as e:
    print(f"Ошибка преобразования: {e}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. TRY/EXCEPT/ELSE/FINALLY
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. TRY/EXCEPT/ELSE/FINALLY")
print("─" * 70)


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  {a} / {b}: Деление на ноль!")
        return None
    except TypeError as e:
        print(f"  {a} / {b}: Неверный тип: {e}")
        return None
    else:
        print(f"  {a} / {b} = {result}")
        return result
    finally:
        print(f"  Завершено.")


divide(10, 2)
divide(10, 0)
divide(10, "2")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. НЕСКОЛЬКО ИСКЛЮЧЕНИЙ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. НЕСКОЛЬКО ИСКЛЮЧЕНИЙ")
print("─" * 70)


def process(value):
    try:
        num = int(value)
        result = 100 / num
    except (ValueError, ZeroDivisionError) as e:
        print(f"  '{value}': {type(e).__name__}: {e}")
    else:
        print(f"  '{value}': Результат = {result}")


process("5")
process("0")
process("abc")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. ИЕРАРХИЯ ИСКЛЮЧЕНИЙ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. ИЕРАРХИЯ ИСКЛЮЧЕНИЙ")
print("─" * 70)

print("""
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── GeneratorExit
 └── Exception
      ├── StopIteration
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── EOFError
      ├── ImportError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── NameError
      ├── OSError
      │    ├── FileNotFoundError
      │    ├── PermissionError
      │    └── TimeoutError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── SyntaxError
      ├── TypeError
      └── ValueError
           └── UnicodeDecodeError
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. RERAISE (ПОВТОРНОЕ ВЫБРАСЫВАНИЕ)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. RERAISE")
print("─" * 70)


def parse_and_divide(a, b):
    try:
        a = int(a)
        b = int(b)
        return a / b
    except ValueError as e:
        print(f"  Не удалось преобразовать: {e}")
        raise  # Пробросить дальше
    except ZeroDivisionError as e:
        print(f"  Деление на ноль: {e}")
        raise RuntimeError("Ошибка деления") from e  # Обернуть


try:
    parse_and_divide("abc", 5)
except ValueError:
    print("  Перехвачено ValueError на верхнем уровне")

try:
    parse_and_divide(10, 0)
except RuntimeError as e:
    print(f"  Перехвачено RuntimeError: {e}")
    print(f"  Причина: {e.__cause__}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. КАСТОМНЫЕ ИСКЛЮЧЕНИЯ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. КАСТОМНЫЕ ИСКЛЮЧЕНИЯ")
print("─" * 70)


class AppError(Exception):
    """Базовое исключение приложения."""

    pass


class ValidationError(AppError):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"Ошибка в поле '{field}': {message}")


class NotFoundError(AppError):
    def __init__(self, resource_id):
        self.resource_id = resource_id
        super().__init__(f"Ресурс {resource_id} не найден")


class DatabaseError(AppError):
    def __init__(self, query, original_error=None):
        self.query = query
        super().__init__(f"Ошибка БД: {query}")
        if original_error:
            self.__cause__ = original_error


# Использование
try:
    raise ValidationError("email", "Неверный формат")
except AppError as e:
    print(f"\n{e}")

try:
    raise NotFoundError(42)
except AppError as e:
    print(f"{e}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. КОНТЕКСТНЫЕ МЕНЕДЖЕРЫ (with)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. КОНТЕКСТНЫЕ МЕНЕДЖЕРЫ")
print("─" * 70)

# Встроенные
import tempfile
import os

# with автоматически закрывает файл
with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
    f.write("Hello, World!")
    temp_path = f.name

print(f"\nФайл создан: {temp_path}")

# Чтение с обработкой ошибок
try:
    with open(temp_path, "r") as f:
        content = f.read()
        print(f"Содержимое: {content}")
except FileNotFoundError:
    print("Файл не найден")
finally:
    os.unlink(temp_path)
    print("Файл удалён")


# Свой контекстный менеджер
class Timer:
    def __init__(self, name="Операция"):
        self.name = name
        import time

        self.time = time

    def __enter__(self):
        self.start = self.time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = self.time.perf_counter() - self.start
        print(f"  {self.name}: {self.elapsed:.4f} сек")
        return False  # Не подавлять исключения


with Timer("Сортировка"):
    sorted([3, 1, 4, 1, 5, 9, 2, 6] * 1000)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. CONTEXTLIB
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. CONTEXTLIB")
print("─" * 70)

from contextlib import contextmanager, suppress


@contextmanager
def managed_resource(name):
    print(f"  Инициализация ресурса: {name}")
    try:
        yield f"Resource({name})"
    except Exception as e:
        print(f"  Ошибка: {e}")
    finally:
        print(f"  Очистка ресурса: {name}")


with managed_resource("DB") as resource:
    print(f"  Работа с: {resource}")

# suppress — подавление исключений
print("\nsuppress(FileNotFoundError):")
with suppress(FileNotFoundError):
    os.remove("nonexistent_file.txt")
    print("  Файл удалён")
print("  Исключение подавлено, код продолжается")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 9. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 9. ПРАКТИЧЕСКИЕ ПРИМЕРЫ")
print("─" * 70)


# 1. Безопасное получение значения из словаря
def safe_get(d, key, default=None):
    try:
        return d[key]
    except KeyError:
        return default


data = {"name": "Alice"}
print(f"\nsafe_get(data, 'name'): {safe_get(data, 'name')}")
print(f"safe_get(data, 'age', 0): {safe_get(data, 'age', 0)}")

# 2. Повторные попытки (retry)
import time


def retry(func, max_attempts=3, delay=0.1):
    for attempt in range(1, max_attempts + 1):
        try:
            return func()
        except Exception as e:
            print(f"  Попытка {attempt}/{max_attempts}: {e}")
            if attempt == max_attempts:
                raise
            time.sleep(delay)


call_count = 0


def flaky_function():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError("Нет соединения")
    return "Успех!"


try:
    result = retry(flaky_function)
    print(f"\nretry: {result}")
except Exception as e:
    print(f"\nretry не помогло: {e}")


# 3. Цепочка ресурсов
class Database:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"  Подключение к {self.name}")
        return self

    def __exit__(self, *args):
        print(f"  Отключение от {self.name}")

    def query(self):
        return "Данные"


class Cache:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"  Открытие кэша {self.name}")
        return self

    def __exit__(self, *args):
        print(f"  Закрытие кэша {self.name}")


print("\nВложенные контекстные менеджеры:")
with Database("main_db") as db:
    with Cache("redis") as cache:
        print(f"  Запрос: {db.query()}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# БАЗОВЫЙ БЛОК
try:
    # код, который может вызвать ошибку
except SpecificError as e:
    # обработка
except (Error1, Error2):
    # несколько ошибок
else:
    # если ошибок не было
finally:
    # выполняется всегда

# ИСКЛЮЧЕНИЯ
raise ValueError("Сообщение")
raise  # пробросить текущее
raise NewError() from e  # обернуть

# КАСТОМНОЕ ИСКЛЮЧЕНИЕ
class MyError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Ошибка: {value}")

# КОНТЕКСТНЫЙ МЕНЕДЖЕР
class MyContext:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, tb):
        return False  # True = подавить исключение

@contextmanager
def my_context():
    setup()
    yield value
    cleanup()

# ПОДАВЛЕНИЕ
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove("file.txt")
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
