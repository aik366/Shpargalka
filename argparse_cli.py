"""
╔══════════════════════════════════════════════════════════════════════╗
║         ШПАРГАЛКА ПО ARGPARSE В PYTHON                               ║
║         Аргументы командной строки — полный справочник               ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import argparse
import sys

print("=" * 70)
print("📚 ШПАРГАЛКА ПО ARGPARSE")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. БАЗОВЫЙ ПАРСЕР
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. БАЗОВЫЙ ПАРСЕР")
print("─" * 70)

print("""
import argparse

parser = argparse.ArgumentParser(
    description="Моя программа для обработки данных",
    epilog="Пример: python script.py input.txt -o output.txt"
)

parser.add_argument("input", help="Входной файл")
parser.add_argument("-o", "--output", help="Выходной файл")

args = parser.parse_args()
print(f"Вход: {args.input}")
print(f"Выход: {args.output}")
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. ТИПЫ АРГУМЕНТОВ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. ТИПЫ АРГУМЕНТОВ")
print("─" * 70)

print("""
# Позиционный (обязательный)
parser.add_argument("filename")

# Опциональный (с коротким и длинным именем)
parser.add_argument("-v", "--verbose")

# Опциональный с дефолтом
parser.add_argument("-c", "--count", default=10, type=int)

# Флаг (True/False)
parser.add_argument("--debug", action="store_true")

# Несколько значений
parser.add_argument("-f", "--files", nargs="+")

# Выбор из вариантов
parser.add_argument("--mode", choices=["train", "test", "eval"])

# Список с разделителем
parser.add_argument("--tags", nargs="*", default=[])
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. ACTION
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. ACTION")
print("─" * 70)

actions = [
    ("store", "Сохранить значение (по умолчанию)"),
    ("store_true", "Установить True"),
    ("store_false", "Установить False"),
    ("store_const", "Сохранить константу"),
    ("append", "Добавить в список"),
    ("count", "Посчитать количество"),
    ("version", "Показать версию"),
]

print(f"\n{'Action':<16} {'Описание'}")
print("-" * 50)
for action, desc in actions:
    print(f"{action:<16} {desc}")

print("""
# Примеры:
parser.add_argument("--verbose", action="store_true")
parser.add_argument("--no-cache", action="store_false")
parser.add_argument("--mode", action="store_const", const="debug")
parser.add_argument("-p", "--path", action="append")
parser.add_argument("-v", "--verbose", action="count")  # -vvv = 3
parser.add_argument("--version", action="version", version="1.0.0")
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. NARGS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. NARGS")
print("─" * 70)

nargs_options = [
    ("N", "Ровно N значений"),
    ("?", "0 или 1 значение"),
    ("*", "0 или более"),
    ("+", "1 или более"),
    ("...", "Все остаточные"),
]

print(f"\n{'Nargs':<10} {'Описание'}")
print("-" * 30)
for nargs, desc in nargs_options:
    print(f"{nargs:<10} {desc}")

print("""
# Примеры:
parser.add_argument("--dims", nargs=3, type=int)     # --dims 1 2 3
parser.add_argument("--file", nargs="?")              # --file или без
parser.add_argument("--tags", nargs="*")              # --tags a b c
parser.add_argument("--files", nargs="+")             # --files a b (минимум 1)
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. TYPE И CHOICES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. TYPE И CHOICES")
print("─" * 70)

print("""
# Встроенные типы
parser.add_argument("--count", type=int)
parser.add_argument("--ratio", type=float)
parser.add_argument("--path", type=Path)

# Пользовательская функция
def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("Должно быть > 0")
    return ivalue

parser.add_argument("--workers", type=positive_int)

# Файл
parser.add_argument("--config", type=argparse.FileType("r"))

# Выбор
parser.add_argument("--format", choices=["json", "yaml", "csv"])
parser.add_argument("--level", choices=range(1, 6), type=int)
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. ГРУППЫ АРГУМЕНТОВ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. ГРУППЫ АРГУМЕНТОВ")
print("─" * 70)

print("""
# Группировка в help
input_group = parser.add_argument_group("Входные данные")
input_group.add_argument("--input", required=True)
input_group.add_argument("--format")

output_group = parser.add_argument_group("Выходные данные")
output_group.add_argument("--output")
output_group.add_argument("--overwrite", action="store_true")

# Взаимоисключающие
group = parser.add_mutually_exclusive_group()
group.add_argument("--verbose", action="store_true")
group.add_argument("--quiet", action="store_true")
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. SUBPARSERS (ПОДКОМАНДЫ)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. ПОДКОМАНДЫ (SUBPARSERS)")
print("─" * 70)

print("""
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", help="Команда")

# create
create_parser = subparsers.add_parser("create", help="Создать запись")
create_parser.add_argument("name")
create_parser.add_argument("--type", default="default")

# delete
delete_parser = subparsers.add_parser("delete", help="Удалить запись")
delete_parser.add_argument("id", type=int)

# list
list_parser = subparsers.add_parser("list", help="Показать все")
list_parser.add_argument("--format", choices=["table", "json"])

args = parser.parse_args()

if args.command == "create":
    print(f"Создаём: {args.name}")
elif args.command == "delete":
    print(f"Удаляем: {args.id}")
elif args.command == "list":
    print("Список записей")
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. ПОЛНЫЙ ПРИМЕР
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. ПОЛНЫЙ ПРИМЕР")
print("─" * 70)

print("""
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="Конвертер файлов",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("input", type=Path, help="Входной файл")
    parser.add_argument("-o", "--output", type=Path, help="Выходной файл")
    parser.add_argument(
        "-f", "--format",
        choices=["json", "csv", "yaml"],
        default="json",
        help="Формат вывода (по умолчанию: json)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="count",
        default=0,
        help="Уровень подробностей (-v, -vv, -vvv)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Не записывать файл"
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Количество потоков"
    )

    args = parser.parse_args()

    if args.verbose >= 2:
        print(f"Вход: {args.input}")
        print(f"Выход: {args.output}")
        print(f"Формат: {args.format}")

    # Логика программы...

if __name__ == "__main__":
    main()
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# БАЗОВЫЙ
parser = argparse.ArgumentParser(description="...")
parser.add_argument("positional")
parser.add_argument("-s", "--short", default="val")
parser.add_argument("--flag", action="store_true")
args = parser.parse_args()

# ТИПЫ
type=int, type=float, type=Path
choices=["a", "b", "c"]
nargs="+", nargs="*", nargs=3

# ACTION
action="store_true"     # Флаг
action="append"         # Список
action="count"          # -vvv = 3
action="version"        # --version

# ГРУППЫ
parser.add_argument_group("Название")
parser.add_mutually_exclusive_group()

# ПОДКОМАНДЫ
subparsers = parser.add_subparsers(dest="cmd")
sub = subparsers.add_parser("create")
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
