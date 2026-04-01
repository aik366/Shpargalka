"""
╔══════════════════════════════════════════════════════════════════════╗
║         ШПАРГАЛКА ПО РАБОТЕ С ФАЙЛОВОЙ СИСТЕМОЙ В PYTHON             ║
║                     os, pathlib — полный справочник                  ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import os
import tempfile
import shutil

print("=" * 70)
print("📚 ШПАРГАЛКА ПО ФАЙЛОВОЙ СИСТЕМЕ")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. PATHLIB (РЕКОМЕНДУЕМЫЙ СПОСОБ)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. PATHLIB — ОСНОВЫ")
print("─" * 70)

from pathlib import Path

# Создание путей
p = Path("C:/python/Shpargalka")
print(f"\nPath: {p}")
print(f"exists(): {p.exists()}")
print(f"is_dir(): {p.is_dir()}")
print(f"is_file(): {p.is_file()}")

# Части пути
p = Path("C:/python/Shpargalka/data_time.py")
print(f"\nPath: {p}")
print(f"p.anchor:    {p.anchor}")
print(f"p.parent:    {p.parent}")
print(f"p.name:      {p.name}")
print(f"p.stem:      {p.stem}")
print(f"p.suffix:    {p.suffix}")
print(f"p.suffixes:  {p.suffixes}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. ОПЕРАЦИИ С ПУТЯМИ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. ОПЕРАЦИИ С ПУТЯМИ")
print("─" * 70)

# Объединение
base = Path("C:/python")
full = base / "Shpargalka" / "data_time.py"
print(f"\nbase / 'Shpargalka' / 'data_time.py': {full}")

# Абсолютный путь
print(f"full.absolute(): {full.absolute()}")

# Разрешение (нормализация)
p = Path("C:/python/./Shpargalka/../Shpargalka/data_time.py")
print(f"resolve(): {p.resolve()}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. СОЗДАНИЕ И УДАЛЕНИЕ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. СОЗДАНИЕ И УДАЛЕНИЕ")
print("─" * 70)

# Временная директория для примеров
tmp = Path(tempfile.mkdtemp())
print(f"Временная директория: {tmp}")

# Создание директории
new_dir = tmp / "subdir" / "nested"
new_dir.mkdir(parents=True, exist_ok=True)
print(f"\nmkdir(parents=True): {new_dir.exists()}")

# Создание файла
new_file = new_dir / "test.txt"
new_file.write_text("Hello, World!", encoding="utf-8")
print(f"write_text: {new_file.read_text(encoding='utf-8')}")

# Удаление
new_file.unlink()
print(f"\nunlink: {new_file.exists()}")

# Удаление директории
shutil.rmtree(tmp)
print(f"rmtree: {Path(tmp).exists()}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. ПЕРЕЧИСЛЕНИЕ ФАЙЛОВ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. ПЕРЕЧИСЛЕНИЕ ФАЙЛОВ")
print("─" * 70)

base = Path("C:/python/Shpargalka")

# iterdir() — содержимое директории
print(f"\niterdir() (первые 5):")
for i, item in enumerate(base.iterdir()):
    if i >= 5:
        break
    print(f"  {'📁' if item.is_dir() else '📄'} {item.name}")

# glob() — поиск по шаблону
print(f"\nglob('*.py'):")
for f in base.glob("*.py"):
    print(f"  {f.name}")

# rglob() — рекурсивный поиск
print(f"\nrglob('*.py'):")
for f in base.rglob("*.py"):
    print(f"  {f}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. ИНФОРМАЦИЯ О ФАЙЛАХ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. ИНФОРМАЦИЯ О ФАЙЛАХ")
print("─" * 70)

p = Path(__file__)
stat = p.stat()

print(f"\nФайл: {p.name}")
print(f"Размер: {stat.st_size:,} байт")

from datetime import datetime

print(f"Изменён: {datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. OS МОДУЛЬ (КЛАССИЧЕСКИЙ ПОДХОД)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. OS МОДУЛЬ")
print("─" * 70)

# Текущая директория
print(f"\nos.getcwd(): {os.getcwd()}")

# Список файлов
print(f"\nos.listdir('.') (первые 5):")
for item in os.listdir(".")[:5]:
    print(f"  {item}")

# Проверки
print(f"\nos.path.exists('.'): {os.path.exists('.')}")
print(f"os.path.isfile(__file__): {os.path.isfile(__file__)}")
print(f"os.path.isdir('.'): {os.path.isdir('.')}")
print(f"os.path.getsize(__file__): {os.path.getsize(__file__):,} байт")

# Разбиение пути
path = "C:/python/Shpargalka/data_time.py"
print(f"\nos.path.dirname('{path}'): {os.path.dirname(path)}")
print(f"os.path.basename('{path}'): {os.path.basename(path)}")
print(f"os.path.splitext('{path}'): {os.path.splitext(path)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. OS.WALK — РЕКУРСИВНЫЙ ОБХОД
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. OS.WALK — РЕКУРСИВНЫЙ ОБХОД")
print("─" * 70)

print(f"\nОбход '{base}' (первые 3 уровня):")
for i, (dirpath, dirnames, filenames) in enumerate(os.walk(base)):
    if i >= 3:
        break
    level = dirpath.replace(str(base), "").count(os.sep)
    indent = "  " * level
    print(f"{indent}📁 {os.path.basename(dirpath)}/")
    for f in filenames[:2]:
        print(f"{indent}  📄 {f}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. ПРАКТИЧЕСКИЕ ПРИМЕРЫ")
print("─" * 70)

# 1. Найти все .py файлы больше 1KB
print("\n1. Файлы .py > 1KB:")
for f in base.glob("*.py"):
    size = f.stat().st_size
    if size > 1024:
        print(f"  {f.name}: {size:,} байт")

# 2. Группировка по расширению
print("\n2. Файлы по расширению:")
extensions = {}
for f in base.iterdir():
    if f.is_file():
        ext = f.suffix
        extensions.setdefault(ext, []).append(f.name)

for ext, files in sorted(extensions.items()):
    print(f"  {ext or '(без расширения)'}: {', '.join(files)}")


# 3. Создание уникального имени файла
def unique_path(directory, filename):
    path = directory / filename
    if path.exists():
        stem = path.stem
        suffix = path.suffix
        counter = 1
        while (directory / f"{stem}_{counter}{suffix}").exists():
            counter += 1
        path = directory / f"{stem}_{counter}{suffix}"
    return path


print(f"\n3. Уникальное имя: {unique_path(base, 'test.txt')}")

# 4. Копирование и перемещение
tmp_dir = Path(tempfile.mkdtemp())
src = tmp_dir / "source.txt"
dst = tmp_dir / "dest.txt"

src.write_text("Hello", encoding="utf-8")
shutil.copy(src, dst)
print(f"\n4. copy: {dst.read_text(encoding='utf-8')}")

shutil.rmtree(tmp_dir)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# PATHLIB (РЕКОМЕНДУЕТСЯ)
from pathlib import Path

p = Path("dir/file.txt")
p.exists()          # Существует?
p.is_file()         # Это файл?
p.is_dir()          # Это директория?
p.mkdir(parents=True)  # Создать директорию
p.unlink()          # Удалить файл
p.read_text()       # Прочитать текст
p.write_text("hi")  # Записать текст
p.stat().st_size    # Размер

# НАВИГАЦИЯ
p.parent            # Родительская директория
p.name              # Имя файла
p.stem              # Имя без расширения
p.suffix            # Расширение
p / "subdir"        # Объединение

# ПОИСК
for f in p.iterdir(): ...
for f in p.glob("*.py"): ...
for f in p.rglob("*.py"): ...  # Рекурсивно

# OS МОДУЛЬ
os.getcwd()         # Текущая директория
os.listdir(".")     # Список файлов
os.path.exists()    # Проверка существования
os.path.join()      # Объединение путей
os.walk()           # Рекурсивный обход
shutil.copy()       # Копирование
shutil.rmtree()     # Удаление директории
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
