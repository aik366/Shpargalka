"""
╔══════════════════════════════════════════════════════════════════════╗
║          ШПАРГАЛКА ПО COMPREHENSIONS В PYTHON                        ║
║     List, dict, set comprehensions — полный справочник               ║
╚══════════════════════════════════════════════════════════════════════╝
"""

print("=" * 70)
print("📚 ШПАРГАЛКА ПО COMPREHENSIONS")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. LIST COMPREHENSIONS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. LIST COMPREHENSIONS")
print("─" * 70)

# Базовый синтаксис: [выражение for элемент in итерируемый]
squares = [x**2 for x in range(10)]
print(f"\nКвадраты: {squares}")

# С условием (filter)
evens = [x for x in range(20) if x % 2 == 0]
print(f"Чётные: {evens}")

# С условием и преобразованием
squares_of_evens = [x**2 for x in range(20) if x % 2 == 0]
print(f"Квадраты чётных: {squares_of_evens}")

# С if-else (ternary)
labels = ["чётное" if x % 2 == 0 else "нечётное" for x in range(10)]
print(f"Чётность: {labels}")

# Вложенные циклы
pairs = [(x, y) for x in range(3) for y in range(3)]
print(f"\nПары (x, y): {pairs}")

# Двумерный массив (матрица)
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"\nМатрица 3x3:")
for row in matrix:
    print(f"  {row}")

# Плоский список из вложенного
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in nested for x in row]
print(f"\nИз вложенного в плоский: {flat}")

# Транспонирование матрицы
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(f"Транспонирование: {transposed}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. DICT COMPREHENSIONS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. DICT COMPREHENSIONS")
print("─" * 70)

# Базовый синтаксис: {ключ: значение for элемент in итерируемый}
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"\nКвадраты (dict): {squares_dict}")

# Из двух списков
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
name_age = {name: age for name, age in zip(names, ages)}
print(f"Из zip: {name_age}")

# С условием
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Только чётные: {even_squares}")

# С if-else
parity = {x: ("чётное" if x % 2 == 0 else "нечётное") for x in range(1, 6)}
print(f"Чётность: {parity}")

# Инвертирование словаря
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"Инверсия: {inverted}")

# Фильтрация словаря
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Dave": 95}
passed = {name: score for name, score in scores.items() if score >= 80}
print(f"Прошедшие (>=80): {passed}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. SET COMPREHENSIONS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. SET COMPREHENSIONS")
print("─" * 70)

# Базовый синтаксис: {выражение for элемент in итерируемый}
unique_squares = {x**2 for x in [-3, -2, -1, 0, 1, 2, 3]}
print(f"\nУникальные квадраты: {unique_squares}")

# Уникальные буквы
word = "programming"
unique_chars = {char for char in word}
print(f"Уникальные буквы в '{word}': {unique_chars}")

# С условием
vowels = {char for char in "hello world" if char in "aeiou"}
print(f"Гласные: {vowels}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. GENERATOR EXPRESSIONS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. GENERATOR EXPRESSIONS")
print("─" * 70)

# Синтаксис: (выражение for элемент in итерируемый)
# Ленивое вычисление — экономия памяти

gen = (x**2 for x in range(5))
print(f"\nГенератор: {gen}")
print(f"Значения: {list(gen)}")

# С sum(), max(), min() — круглые скобки не нужны
total = sum(x**2 for x in range(100))
print(f"Сумма квадратов 0-99: {total}")

max_val = max(x for x in range(10) if x % 3 == 0)
print(f"Максимум кратных 3: {max_val}")

# Join с генератором
result = ", ".join(str(x) for x in range(5))
print(f"Join: {result}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. ВЛОЖЕННЫЕ COMPREHENSIONS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. ВЛОЖЕННЫЕ COMPREHENSIONS")
print("─" * 70)

# Группировка по ключу
data = [("fruit", "apple"), ("fruit", "banana"), ("animal", "cat"), ("animal", "dog")]
grouped = {key: [v for k, v in data if k == key] for key in set(k for k, v in data)}
print(f"\nГруппировка: {grouped}")

# Подсчёт вложенных элементов
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = sum(sum(row) for row in matrix)
print(f"Сумма матрицы: {total}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. ПРАКТИЧЕСКИЕ ПРИМЕРЫ")
print("─" * 70)

# 1. Фильтрация строк
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = [w for w in words if len(w) > 5]
print(f"\nДлинные слова (>5): {long_words}")

# 2. Извлечение данных
users = [
    {"name": "Alice", "age": 25, "active": True},
    {"name": "Bob", "age": 30, "active": False},
    {"name": "Charlie", "age": 35, "active": True},
]
active_names = [u["name"] for u in users if u["active"]]
print(f"Активные пользователи: {active_names}")

# 3. Частотный анализ
text = "hello world hello python world hello"
word_counts = {word: text.split().count(word) for word in set(text.split())}
print(f"\nЧастота слов: {word_counts}")

# 4. Числа Фибоначчи
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]
print(f"\nФибоначчи: {fib[:10]}")

# 5. Пифагоровы тройки
pythagorean = [
    (a, b, c)
    for a in range(1, 20)
    for b in range(a, 20)
    for c in range(1, 20)
    if a**2 + b**2 == c**2
]
print(f"Пифагоровы тройки: {pythagorean}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. КОГДА ИСПОЛЬЗОВАТЬ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. КОГДА ИСПОЛЬЗОВАТЬ")
print("─" * 70)

print("""
✅ Используйте comprehensions когда:
  • Простое преобразование/фильтрация (1-2 строки)
  • Нужно создать новую коллекцию
  • Код остаётся читаемым

❌ Не используйте когда:
  • Сложная логика с множеством условий
  • Нужно более 2 вложенных циклов
  • Побочные эффекты (print, запись в файл)
  • Лучше использовать обычный for цикл

💡 Generator expressions когда:
  • Нужна экономия памяти
  • Данные используются один раз
  • Передаёте в sum(), max(), min(), any(), all()
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# LIST
[x**2 for x in range(10)]              # Преобразование
[x for x in range(10) if x % 2 == 0]   # Фильтрация
[x if x % 2 == 0 else 0 for x in range(10)]  # if-else

# DICT
{x: x**2 for x in range(5)}            # Создание
{k: v for k, v in d.items() if v > 0}  # Фильтрация
{v: k for k, v in d.items()}           # Инверсия

# SET
{x**2 for x in [-2, -1, 0, 1, 2]}      # Уникальные значения

# GENERATOR
(x**2 for x in range(10))              # Ленивое вычисление
sum(x**2 for x in range(10))           # С функциями

# ВЛОЖЕННЫЕ
[[i*j for j in range(3)] for i in range(3)]  # Матрица
[x for row in matrix for x in row]     # Flatten
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
