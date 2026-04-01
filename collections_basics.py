"""
╔══════════════════════════════════════════════════════════════════════╗
║             ШПАРГАЛКА ПО КОЛЛЕКЦИЯМ В PYTHON                         ║
║         list, dict, set, tuple — полный справочник                   ║
╚══════════════════════════════════════════════════════════════════════╝
"""

print("=" * 70)
print("📚 ШПАРГАЛКА ПО КОЛЛЕКЦИЯМ В PYTHON")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. СПИСКИ (list) — изменяемые, упорядоченные
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. СПИСКИ (list)")
print("─" * 70)

# Создание
fruits = ["яблоко", "банан", "вишня"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, None, [1, 2]]
empty = []
from_range = list(range(5))

print(f"\nСоздание: {fruits}")
print(f"Из range: {from_range}")
print(f"Пустой: {empty}")

# Доступ по индексу
print(f"\nfruits[0]:    {fruits[0]}")
print(f"fruits[-1]:   {fruits[-1]}")
print(f"fruits[1:3]:  {fruits[1:3]}")
print(f"fruits[:2]:   {fruits[:2]}")
print(f"fruits[::2]:  {fruits[::2]}")
print(f"fruits[::-1]: {fruits[::-1]}")

# Методы списков
lst = [3, 1, 4, 1, 5, 9, 2, 6]

lst.append(7)  # Добавить в конец
lst.insert(0, 0)  # Вставить по индексу
lst.extend([8, 9])  # Расширить другим списком
lst.remove(1)  # Удалить первое вхождение
popped = lst.pop()  # Удалить и вернуть последний
lst.pop(0)  # Удалить по индексу
lst.sort()  # Сортировка на месте
lst.reverse()  # Разворот на месте

print(f"\nПосле операций: {lst}")
print(f"Popped: {popped}")

# Полезные методы
print(f"\nlen(lst):     {len(lst)}")
print(f"lst.count(1):  {lst.count(1)}")
print(f"lst.index(5):  {lst.index(5)}")
print(f"5 in lst:      {5 in lst}")

# Копирование
original = [1, 2, 3]
shallow_copy = original.copy()
slice_copy = original[:]
list_copy = list(original)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. КОРТЕЖИ (tuple) — неизменяемые, упорядоченные
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. КОРТЕЖИ (tuple)")
print("─" * 70)

# Создание
point = (3, 4)
single = (42,)  # Запятая обязательна!
not_tuple = 42  # Это просто число!
empty_tuple = ()
from_list = tuple([1, 2, 3])

print(f"\npoint: {point}")
print(f"single: {single}, type: {type(single)}")
print(f"not_tuple: {not_tuple}, type: {type(not_tuple)}")

# Распаковка
x, y = point
print(f"\nРаспаковка: x={x}, y={y}")

# Распаковка с *
first, *middle, last = [1, 2, 3, 4, 5]
print(f"first={first}, middle={middle}, last={last}")

# Методы (только 2)
t = (1, 2, 2, 3, 2)
print(f"\nt.count(2): {t.count(2)}")
print(f"t.index(3): {t.index(3)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. СЛОВАРИ (dict) — пары ключ-значение
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. СЛОВАРИ (dict)")
print("─" * 70)

# Создание
person = {"name": "Алиса", "age": 30, "city": "Москва"}
from_constructor = dict(name="Боб", age=25)
from_pairs = dict([("a", 1), ("b", 2)])
empty_dict = {}

print(f"\nperson: {person}")
print(f"from_constructor: {from_constructor}")

# Доступ
print(f"\nperson['name']:    {person['name']}")
print(f"person.get('age'):  {person.get('age')}")
print(f"person.get('job'):  {person.get('job')}")
print(f"person.get('job', 'N/A'): {person.get('job', 'N/A')}")

# Добавление/изменение
person["job"] = "Разработчик"
person["age"] = 31
print(f"\nПосле изменений: {person}")

# Удаление
removed = person.pop("city")
print(f"Удалено: {removed}")
print(f"Осталось: {person}")

# Методы
d = {"a": 1, "b": 2, "c": 3}

print(f"\nkeys():   {list(d.keys())}")
print(f"values(): {list(d.values())}")
print(f"items():  {list(d.items())}")

# Перебор словаря
print("\nПеребор:")
for key, value in d.items():
    print(f"  {key} → {value}")

# Слияние (Python 3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = d1 | d2
print(f"\nСлияние (|): {merged}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. МНОЖЕСТВА (set) — уникальные, неупорядоченные
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. МНОЖЕСТВА (set)")
print("─" * 70)

# Создание
s1 = {1, 2, 3, 3, 3}  # Дубликаты удаляются
s2 = set([2, 3, 4, 5])
empty_set = set()  # {} — это пустой dict!

print(f"\ns1: {s1}")
print(f"s2: {s2}")

# Операции
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"\nОбъединение (|):        {a | b}")
print(f"Пересечение (&):         {a & b}")
print(f"Разность (-):            {a - b}")
print(f"Симметричная разность (^): {a ^ b}")

# Методы
s = {1, 2, 3}
s.add(4)
s.update([5, 6])
s.discard(2)  # Не ошибка, если нет
s.remove(3)  # KeyError, если нет

print(f"\nПосле операций: {s}")

# Проверки
print(f"\n1 in s: {1 in s}")
print(f"Подмножество: {{1}} <= s: { {1} <= s }")
print(f"Надмножество: s >= {{1, 4}}: {s >= {1, 4}}")

# Удаление дубликатов из списка
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))
print(f"\nУдаление дубликатов: {nums} → {unique}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. СРАВНЕНИЕ КОЛЛЕКЦИЙ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. СРАВНЕНИЕ КОЛЛЕКЦИЙ")
print("─" * 70)

comparison = [
    ("list", "[]", "Да", "Да", "Да", "Да"),
    ("tuple", "()", "Нет", "Да", "Да", "Да"),
    ("dict", "{}", "Да", "Нет", "Пары ключ-значение", "Да"),
    ("set", "set()", "Да", "Нет", "Нет", "Нет"),
]

print(
    f"\n{'Тип':<10} {'Синтаксис':<10} {'Изменяем':<10} {'Упоряд':<8} {'Дубликаты':<18} {'Индекс':<8}"
)
print("-" * 70)
for row in comparison:
    print(
        f"{row[0]:<10} {row[1]:<10} {row[2]:<10} {row[3]:<8} {row[4]:<18} {row[5]:<8}"
    )

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. ПОЛЕЗНЫЕ ПРИЁМЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. ПОЛЕЗНЫЕ ПРИЁМЫ")
print("─" * 70)

# Распаковка вложенных структур
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
print("\nРаспаковка в цикле:")
for name, age in data:
    print(f"  {name}: {age}")

# zip — объединение
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = dict(zip(names, ages))
print(f"\nzip в dict: {combined}")

# enumerate — индекс + значение
colors = ["красный", "зелёный", "синий"]
print("\nenumerate:")
for i, color in enumerate(colors, 1):
    print(f"  {i}. {color}")

# Сортировка словаря
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
by_value = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(f"\nСортировка по значению: {by_value}")

# Фильтрация
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in nums if n % 2 == 0]
print(f"\nЧётные числа: {evens}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# СПИСОК
lst = [1, 2, 3]
lst.append(4)          # Добавить в конец
lst.insert(0, 0)       # Вставить по индексу
lst.extend([5, 6])     # Расширить
lst.pop()              # Удалить последний
lst.remove(2)          # Удалить по значению
lst.sort()             # Сортировка
lst.reverse()          # Разворот

# КОРТЕЖ
t = (1, 2, 3)
x, y, z = t            # Распаковка
first, *rest = t       # Распаковка с *

# СЛОВАРЬ
d = {"a": 1, "b": 2}
d["c"] = 3             # Добавить
d.get("x", "default")  # Безопасный доступ
d.pop("a")             # Удалить
d1 | d2                # Слияние (3.9+)

# МНОЖЕСТВО
s = {1, 2, 3}
s.add(4)               # Добавить
s.discard(2)           # Удалить (без ошибки)
a | b, a & b, a - b    # Объединение, пересечение, разность
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
