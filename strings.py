"""
╔══════════════════════════════════════════════════════════════════════╗
║              ШПАРГАЛКА ПО СТРОКАМ В PYTHON                           ║
║         Методы, форматирование, приёмы работы                        ║
╚══════════════════════════════════════════════════════════════════════╝
"""

print("=" * 70)
print("📚 ШПАРГАЛКА ПО СТРОКАМ В PYTHON")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. СОЗДАНИЕ СТРОК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. СОЗДАНИЕ СТРОК")
print("─" * 70)

s1 = "Одинарные кавычки"
s2 = "Двойные кавычки"
s3 = """Многострочная
строка"""
s4 = r"Сырая строка: \n не работает"
s5 = f"Форматированная: {2 + 2}"
s6 = str(42)

print(f"s1: {s1}")
print(f"s2: {s2}")
print(f"s3:\n{s3}")
print(f"s4: {s4}")
print(f"s5: {s5}")
print(f"s6: {s6}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. ИНДЕКСАЦИЯ И СРЕЗЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. ИНДЕКСАЦИЯ И СРЕЗЫ")
print("─" * 70)

text = "Python Programming"

print(f"\ntext: '{text}'")
print(f"text[0]:    '{text[0]}'")
print(f"text[-1]:   '{text[-1]}'")
print(f"text[0:6]:  '{text[0:6]}'")
print(f"text[7:]:   '{text[7:]}'")
print(f"text[:6]:   '{text[:6]}'")
print(f"text[::2]:  '{text[::2]}'")
print(f"text[::-1]: '{text[::-1]}'")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. ОСНОВНЫЕ МЕТОДЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. ОСНОВНЫЕ МЕТОДЫ")
print("─" * 70)

s = "  Hello, World!  "

print(f"\nОригинал: '{s}'")
print(f"strip():      '{s.strip()}'")
print(f"lstrip():     '{s.lstrip()}'")
print(f"rstrip():     '{s.rstrip()}'")

s2 = "hello, world!"
print(f"\nupper():      '{s2.upper()}'")
print(f"lower():      '{s2.lower()}'")
print(f"capitalize(): '{s2.capitalize()}'")
print(f"title():      '{s2.title()}'")
print(f"swapcase():   '{s2.swapcase()}'")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. ПОИСК И ЗАМЕНА
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. ПОИСК И ЗАМЕНА")
print("─" * 70)

text = "Python — это Python, и это здорово!"

print(f"\nОригинал: '{text}'")
print(f"find('Python'):     {text.find('Python')}")
print(f"rfind('Python'):    {text.rfind('Python')}")
print(f"index('Python'):    {text.index('Python')}")
print(f"count('Python'):    {text.count('Python')}")
print(f"startswith('Py'):   {text.startswith('Py')}")
print(f"endswith('!'):      {text.endswith('!')}")

print(f"\nreplace('Python', 'JS'): '{text.replace('Python', 'JS')}'")
print(f"replace (1 раз): '{text.replace('Python', 'JS', 1)}'")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. РАЗБИЕНИЕ И ОБЪЕДИНЕНИЕ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. РАЗБИЕНИЕ И ОБЪЕДИНЕНИЕ")
print("─" * 70)

text = "apple,banana,cherry,date"

# split
parts = text.split(",")
print(f"\nsplit(','): {parts}")

text2 = "one\ntwo\tthree"
print(f"split() (по пробелам): {text2.split()}")

# partition
text3 = "key=value"
key, sep, val = text3.partition("=")
print(f"partition('='): key='{key}', sep='{sep}', val='{val}'")

# join
words = ["Python", "is", "awesome"]
joined = " ".join(words)
print(f"\njoin(' '): '{joined}'")

csv = ",".join(words)
print(f"join(','): '{csv}'")

lines = "\n".join(words)
print(f"join('\\n'):\n{lines}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. ПРОВЕРКИ (is_* методы)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. ПРОВЕРКИ (is_* методы)")
print("─" * 70)

tests = [
    ("12345", "isdigit"),
    ("abc123", "isalnum"),
    ("hello", "isalpha"),
    ("hello", "islower"),
    ("HELLO", "isupper"),
    ("Hello World", "istitle"),
    ("   ", "isspace"),
    ("name", "isidentifier"),
]

for value, method in tests:
    result = getattr(value, method)()
    print(f"'{value}'.{method}() → {result}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. ВЫРАВНИВАНИЕ И ЗАПОЛНЕНИЕ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. ВЫРАВНИВАНИЕ И ЗАПОЛНЕНИЕ")
print("─" * 70)

text = "Python"

print(f"\nОригинал: '{text}'")
print(f"ljust(10):  '{text.ljust(10)}'")
print(f"rjust(10):  '{text.rjust(10)}'")
print(f"center(10): '{text.center(10)}'")
print(f"center(10, '*'): '{text.center(10, '*')}'")
print(f"zfill(10):  '{text.zfill(10)}'")

# Числа с ведущими нулями
print(f"\n'42'.zfill(5): '42'.zfill(5)")
print(f"'-42'.zfill(5): '-42'.zfill(5)")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. ПОЛЕЗНЫЕ ПРИЁМЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. ПОЛЕЗНЫЕ ПРИЁМЫ")
print("─" * 70)

# Удаление лишних пробелов
text = "  hello   world   this   is   python  "
cleaned = " ".join(text.split())
print(f"\nУдаление лишних пробелов:")
print(f"  Было: '{text}'")
print(f"  Стало: '{cleaned}'")

# Трансляция символов (maketrans/translate)
text = "hello world"
trans = str.maketrans("hw", "HW")
print(f"\ntranslate: '{text.translate(trans)}'")

# Удаление знаков препинания
import string

text = "Hello, World! How's it going?"
no_punct = text.translate(str.maketrans("", "", string.punctuation))
print(f"Без пунктуации: '{no_punct}'")

# Повторение строки
print(f"\n'ab' * 5: {'ab' * 5}")
print(f"'-' * 30: {'-' * 30}")

# Конкатенация
s1, s2, s3 = "Hello", " ", "World"
print(f"Конкатенация: {s1 + s2 + s3}")

# Проверка вхождения
text = "Python Programming"
print(f"\n'Prog' in text: {'Prog' in text}")
print(f"'Java' not in text: {'Java' not in text}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 9. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 9. ПРАКТИЧЕСКИЕ ПРИМЕРЫ")
print("─" * 70)


# 1. Палиндром
def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


print(f"\nПалиндромы:")
print(f"  'А роза упала на лапу Азора': {is_palindrome('А роза упала на лапу Азора')}")
print(f"  'hello': {is_palindrome('hello')}")

# 2. Подсчёт символов
text = "hello world"
counts = {char: text.count(char) for char in set(text) if char != " "}
print(f"\nПодсчёт символов в '{text}': {counts}")

# 3. Капитализация каждого слова
text = "hello world from python"
print(f"\ntitle(): '{text.title()}'")

# 4. Извлечение чисел из строки
text = "Цена: 1234 рубля, скидка 20%"
digits = "".join(c for c in text if c.isdigit())
print(f"\nЧисла из '{text}': {digits}")

# 5. Сокращение строки
text = "Это очень длинная строка которая не помещается"
print(f"\nСокращение: '{text[:20]}...'")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# ОСНОВНЫЕ МЕТОДЫ
s.strip()        # Убрать пробелы по краям
s.upper()        # Верхний регистр
s.lower()        # Нижний регистр
s.capitalize()   # Первая буква заглавная
s.title()        # Каждое слово с заглавной

# ПОИСК
s.find("sub")    # Индекс первого вхождения (-1 если нет)
s.index("sub")   # Как find, но ValueError если нет
s.count("sub")   # Количество вхождений
s.startswith("x")# Начинается ли с...
s.endswith("x")  # Заканчивается ли на...

# ЗАМЕНА И РАЗБИЕНИЕ
s.replace("old", "new")
s.split(",")     # Разбить по разделителю
s.split()        # Разбить по пробелам
",".join(list)   # Объединить список

# ПРОВЕРКИ
s.isdigit()      # Только цифры
s.isalpha()      # Только буквы
s.isalnum()      # Буквы или цифры
s.islower()      # Только строчные
s.isupper()      # Только заглавные
s.isspace()      # Только пробелы
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
