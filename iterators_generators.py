"""
╔══════════════════════════════════════════════════════════════════════╗
║       ШПАРГАЛКА ПО ИТЕРАТОРАМ И ГЕНЕРАТОРАМ В PYTHON                 ║
║              yield, itertools, генераторные выражения                ║
╚══════════════════════════════════════════════════════════════════════╝
"""

from itertools import (
    count,
    cycle,
    repeat,
    chain,
    islice,
    tee,
    combinations,
    permutations,
    groupby,
    accumulate,
    product,
)

print("=" * 70)
print("📚 ШПАРГАЛКА ПО ИТЕРАТОРАМ И ГЕНЕРАТОРАМ")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. ИТЕРАТОРЫ — ОСНОВЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. ИТЕРАТОРЫ — ОСНОВЫ")
print("─" * 70)

# Итерируемый объект → итератор
lst = [1, 2, 3]
it = iter(lst)

print(f"next(it): {next(it)}")
print(f"next(it): {next(it)}")
print(f"next(it): {next(it)}")

try:
    next(it)
except StopIteration:
    print("next(it): StopIteration — элементы закончились")

# Проверка
from collections.abc import Iterator, Iterable

print(f"\nisinstance([1,2,3], Iterable): {isinstance([1, 2, 3], Iterable)}")
print(f"isinstance(iter([1,2,3]), Iterator): {isinstance(iter([1, 2, 3]), Iterator)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. ГЕНЕРАТОРЫ (yield)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. ГЕНЕРАТОРЫ (yield)")
print("─" * 70)


def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1


gen = count_up_to(5)
print(f"\ncount_up_to(5): {list(gen)}")

# Генератор — это итератор
print(f"isinstance(gen, Iterator): {isinstance(gen, Iterator)}")


# Генератор с состоянием
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(f"\nfibonacci(10): {list(fibonacci(10))}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. YIELD FROM
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. YIELD FROM")
print("─" * 70)


def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


nested = [1, [2, 3], [4, [5, 6]], 7]
print(f"\nflatten({nested}): {list(flatten(nested))}")


# Делегирование другому генератору
def sub_gen():
    yield "a"
    yield "b"
    return "result"


def main_gen():
    result = yield from sub_gen()
    yield f"sub_gen вернул: {result}"


print(f"main_gen: {list(main_gen())}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. БЕСКОНЕЧНЫЕ ИТЕРАТОРЫ (itertools)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. БЕСКОНЕЧНЫЕ ИТЕРАТОРЫ")
print("─" * 70)

# count — бесконечный счётчик
print(f"\ncount(10, 3) → {list(islice(count(10, 3), 5))}")

# cycle — бесконечный цикл
print(f"cycle('ABCD') → {list(islice(cycle('ABCD'), 8))}")

# repeat — повторение
print(f"repeat('Hi', 4) → {list(repeat('Hi', 4))}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. ОБЪЕДИНЕНИЕ И НАРЕЗКА
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. ОБЪЕДИНЕНИЕ И НАРЕЗКА")
print("─" * 70)

# chain — объединение
a = [1, 2, 3]
b = [4, 5, 6]
print(f"\nchain({a}, {b}) → {list(chain(a, b))}")

# chain.from_iterable
nested = [[1, 2], [3, 4], [5, 6]]
print(f"chain.from_iterable → {list(chain.from_iterable(nested))}")

# islice — срез итератора
print(f"\nislice(count(0), 5, 10) → {list(islice(count(0), 5, 10))}")
print(f"islice('ABCDEFG', 2, None) → {list(islice('ABCDEFG', 2, None))}")

# tee — копирование итератора
it1, it2 = tee([1, 2, 3, 4, 5], 2)
print(f"\ntee: {list(it1)} и {list(it2)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. КОМБИНАТОРИКА
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. КОМБИНАТОРИКА")
print("─" * 70)

items = ["A", "B", "C"]

print(f"\npermutations({items}) → {list(permutations(items))}")
print(f"combinations({items}, 2) → {list(combinations(items, 2))}")
print(f"product('AB', '12') → {list(product('AB', '12'))}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. GROUPBY
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. GROUPBY")
print("─" * 70)

# Группировка (данные должны быть отсортированы!)
data = [
    ("fruit", "apple"),
    ("fruit", "banana"),
    ("animal", "cat"),
    ("animal", "dog"),
    ("fruit", "cherry"),
]

# Сортировка перед группировкой
data.sort(key=lambda x: x[0])

print("\nГруппировка по типу:")
for key, group in groupby(data, key=lambda x: x[0]):
    items = [g[1] for g in group]
    print(f"  {key}: {items}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. ACCUMULATE
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. ACCUMULATE")
print("─" * 70)

nums = [1, 2, 3, 4, 5]

print(f"\naccumulate({nums}) → {list(accumulate(nums))}")

import operator

print(f"accumulate({nums}, mul) → {list(accumulate(nums, operator.mul))}")
print(f"accumulate({nums}, max) → {list(accumulate(nums, max))}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 9. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 9. ПРАКТИЧЕСКИЕ ПРИМЕРЫ")
print("─" * 70)


# 1. Чтение большого файла по частям
def read_chunks(file_path, chunk_size=1024):
    with open(file_path, "r", encoding="utf-8") as f:
        while chunk := f.read(chunk_size):
            yield chunk


# 2. Генератор простых чисел
def primes():
    yield 2
    found = [2]
    n = 3
    while True:
        if all(n % p != 0 for p in found if p * p <= n):
            found.append(n)
            yield n
        n += 2


print(f"\nПервые 10 простых: {list(islice(primes(), 10))}")


# 3. Скользящее окно
def sliding_window(iterable, size):
    it = iter(iterable)
    window = list(islice(it, size))
    if len(window) == size:
        yield tuple(window)
    for item in it:
        window.append(item)
        window.pop(0)
        yield tuple(window)


print(f"\nsliding_window([1,2,3,4,5], 3): {list(sliding_window([1, 2, 3, 4, 5], 3))}")


# 4. Пагинация
def paginate(items, page_size):
    it = iter(items)
    while chunk := list(islice(it, page_size)):
        yield chunk


data = list(range(1, 21))
print(f"\nПагинация (по 7):")
for i, page in enumerate(paginate(data, 7), 1):
    print(f"  Страница {i}: {page}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# ГЕНЕРАТОР
def gen():
    yield 1
    yield 2

g = gen()
next(g)        # 1
list(g)        # [2]

# YIELD FROM
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

# ITERTOOLS
count(start, step)     # Бесконечный счётчик
cycle(iterable)        # Бесконечный цикл
repeat(elem, n)        # Повторение n раз
chain(a, b)            # Объединение
islice(iter, start, stop)  # Срез
tee(iter, n)           # n копий
permutations(iter)     # Перестановки
combinations(iter, r)  # Комбинации
product(a, b)          # Декартово произведение
groupby(data, key)     # Группировка
accumulate(data, func) # Накопление
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
