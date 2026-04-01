"""
╔══════════════════════════════════════════════════════════════════════╗
║           ШПАРГАЛКА ПО РАБОТЕ С ФАЙЛАМИ В PYTHON                     ║
║         Чтение, запись, контекстные менеджеры, pathlib               ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import os
import tempfile

print("=" * 70)
print("📚 ШПАРГАЛКА ПО РАБОТЕ С ФАЙЛАМИ")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. ОТКРЫТИЕ ФАЙЛОВ (ВСТРОЕННАЯ open())
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. РЕЖИМЫ ОТКРЫТИЯ")
print("─" * 70)

modes = [
    ("r", "Чтение (по умолчанию)"),
    ("w", "Запись (перезаписывает)"),
    ("a", "Дозапись (в конец)"),
    ("x", "Создание (ошибка если есть)"),
    ("b", "Бинарный режим"),
    ("t", "Текстовый режим (по умолчанию)"),
    ("+", "Чтение и запись"),
]

print(f"\n{'Режим':<8} {'Описание'}")
print("-" * 40)
for mode, desc in modes:
    print(f"{mode:<8} {desc}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. ЗАПИСЬ И ЧТЕНИЕ ТЕКСТОВЫХ ФАЙЛОВ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. ЗАПИСЬ И ЧТЕНИЕ")
print("─" * 70)

# Создаём временный файл для примеров
with tempfile.NamedTemporaryFile(
    mode="w", delete=False, suffix=".txt", encoding="utf-8"
) as f:
    temp_file = f.name
    f.write("Строка 1\n")
    f.write("Строка 2\n")
    f.write("Строка 3\n")

print(f"Файл: {temp_file}")

# Чтение всего файла
with open(temp_file, "r", encoding="utf-8") as f:
    content = f.read()
    print(f"\nread():\n{content}")

# Чтение построчно
with open(temp_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"readlines(): {lines}")

# Чтение построчно (итерация)
with open(temp_file, "r", encoding="utf-8") as f:
    print("\nПострочная итерация:")
    for i, line in enumerate(f, 1):
        print(f"  {i}: {line.strip()}")

# Дозапись
with open(temp_file, "a", encoding="utf-8") as f:
    f.write("Строка 4\n")

with open(temp_file, "r", encoding="utf-8") as f:
    print(f"\nПосле дозаписи:\n{f.read()}")

os.unlink(temp_file)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. ЗАПИСЬ НЕСКОЛЬКИХ СТРОК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. WRITELINES И PRINT")
print("─" * 70)

with tempfile.NamedTemporaryFile(
    mode="w", delete=False, suffix=".txt", encoding="utf-8"
) as f:
    temp_file = f.name
    lines = ["Первая\n", "Вторая\n", "Третья\n"]
    f.writelines(lines)

with open(temp_file, "r", encoding="utf-8") as f:
    print(f"writelines():\n{f.read()}")

# print в файл
with open(temp_file, "w", encoding="utf-8") as f:
    print("Hello", "World", file=f)
    print("Python", "is", "great", file=f, sep="-")

with open(temp_file, "r", encoding="utf-8") as f:
    print(f"\nprint в файл:\n{f.read()}")

os.unlink(temp_file)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. БИНАРНЫЕ ФАЙЛЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. БИНАРНЫЕ ФАЙЛЫ")
print("─" * 70)

with tempfile.NamedTemporaryFile(delete=False, suffix=".bin") as f:
    temp_file = f.name
    f.write(b"\x00\x01\x02\x03\x04\x05")

with open(temp_file, "rb") as f:
    data = f.read()
    print(f"\nread(): {data}")

with open(temp_file, "rb") as f:
    chunk = f.read(3)
    print(f"read(3): {chunk}")
    chunk = f.read(3)
    print(f"read(3): {chunk}")

os.unlink(temp_file)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. ПОЗИЦИОНИРОВАНИЕ В ФАЙЛЕ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. SEEK И TELL")
print("─" * 70)

with tempfile.NamedTemporaryFile(mode="wb", delete=False) as f:
    temp_file = f.name
    f.write(b"Hello, World!")

with open(temp_file, "rb") as f:
    print(f"\ntell() в начале: {f.tell()}")
    f.seek(7)
    print(f"seek(7), tell(): {f.tell()}")
    print(f"read(): {f.read()}")
    f.seek(0)
    print(f"seek(0), read(5): {f.read(5)}")

os.unlink(temp_file)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. РАБОТА С CSV
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. CSV ФАЙЛЫ")
print("─" * 70)

import csv

with tempfile.NamedTemporaryFile(
    mode="w", delete=False, suffix=".csv", encoding="utf-8", newline=""
) as f:
    temp_file = f.name
    writer = csv.writer(f)
    writer.writerow(["Имя", "Возраст", "Город"])
    writer.writerow(["Алиса", 30, "Москва"])
    writer.writerow(["Боб", 25, "Питер"])

print("Запись CSV:")
with open(temp_file, "r", encoding="utf-8") as f:
    print(f.read())

print("Чтение CSV:")
with open(temp_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"  {row}")

os.unlink(temp_file)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. ПОЛЕЗНЫЕ ПРИЁМЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. ПОЛЕЗНЫЕ ПРИЁМЫ")
print("─" * 70)

# Чтение больших файлов по частям
print("\nЧтение по частям:")
with tempfile.NamedTemporaryFile(
    mode="w", delete=False, suffix=".txt", encoding="utf-8"
) as f:
    temp_file = f.name
    f.write("A" * 100)

with open(temp_file, "r", encoding="utf-8") as f:
    while chunk := f.read(20):
        print(f"  [{len(chunk)} символов]")

os.unlink(temp_file)

# Проверка существования файла
print(f"\nos.path.exists('nonexistent'): {os.path.exists('nonexistent')}")

# Размер файла
size = os.path.getsize(__file__)
print(f"Размер этого файла: {size:,} байт")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# ЧТЕНИЕ
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()        # Весь файл
    lines = f.readlines()     # Список строк
    for line in f:            # Построчно (эффективно)
        pass

# ЗАПИСЬ
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write('текст')
    f.writelines(['строка\\n'])
    print('текст', file=f)

# ДОЗАПИСЬ
with open('file.txt', 'a', encoding='utf-8') as f:
    f.write('новая строка\\n')

# БИНАРНЫЙ
with open('file.bin', 'rb') as f:
    data = f.read()

# ПОЗИЦИОНИРОВАНИЕ
f.seek(0)       # В начало
f.seek(10)      # На позицию 10
f.tell()        # Текущая позиция

# ПРОВЕРКИ
os.path.exists('file.txt')
os.path.isfile('file.txt')
os.path.getsize('file.txt')
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
