"""
╔══════════════════════════════════════════════════════════════════════╗
║        ШПАРГАЛКА ПО РЕГУЛЯРНЫМ ВЫРАЖЕНИЯМ В PYTHON                   ║
║                    Модуль re — полный справочник                     ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import re

print("=" * 70)
print("📚 ШПАРГАЛКА ПО РЕГУЛЯРНЫМ ВЫРАЖЕНИЯМ")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. ОСНОВНЫЕ ФУНКЦИИ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. ОСНОВНЫЕ ФУНКЦИИ")
print("─" * 70)

text = "Мой email: test@example.com, а также info@test.org"

# re.search — первое совпадение
match = re.search(r"\w+@\w+\.\w+", text)
print(f"\nsearch: {match.group() if match else None}")

# re.match — только в начале строки
match = re.match(r"Mой", text)
print(f"match 'Мой': {match.group() if match else None}")
match = re.match(r"email", text)
print(f"match 'email': {match.group() if match else None}")

# re.findall — все совпадения
emails = re.findall(r"\w+@\w+\.\w+", text)
print(f"findall: {emails}")

# re.finditer — итератор Match объектов
print("\nfinditer:")
for m in re.finditer(r"\w+@\w+\.\w+", text):
    print(f"  '{m.group()}' на позиции {m.start()}-{m.end()}")

# re.sub — замена
result = re.sub(r"\w+@\w+\.\w+", "[EMAIL]", text)
print(f"\nsub: {result}")

# re.split — разбиение
parts = re.split(r"[,\s]+", "one, two  three four")
print(f"split: {parts}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. СПЕЦСИМВОЛЫ И МЕТАСИМВОЛЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. СПЕЦСИМВОЛЫ")
print("─" * 70)

patterns = [
    (r".", "Любой символ (кроме \\n)"),
    (r"\d", "Цифра [0-9]"),
    (r"\D", "Не цифра [^0-9]"),
    (r"\w", "Слово [a-zA-Z0-9_]"),
    (r"\W", "Не слово [^a-zA-Z0-9_]"),
    (r"\s", "Пробел [ \\t\\n\\r\\f\\v]"),
    (r"\S", "Не пробел"),
    (r"^", "Начало строки"),
    (r"$", "Конец строки"),
    (r"\b", "Граница слова"),
    (r"\B", "Не граница слова"),
]

print(f"\n{'Символ':<8} {'Описание'}")
print("-" * 40)
for sym, desc in patterns:
    print(f"{sym:<8} {desc}")

# Примеры
test_text = "Hello 123 World_456"
print(f"\nТекст: '{test_text}'")
print(f"\\d+: {re.findall(r'\d+', test_text)}")
print(f"\\w+: {re.findall(r'\w+', test_text)}")
print(f"\\s+: {re.findall(r'\s+', test_text)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. КВАНТИФИКАТОРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. КВАНТИФИКАТОРЫ")
print("─" * 70)

text = "a ab abb abbb abbbb"

quantifiers = [
    (r"a*", "0 или более"),
    (r"a+", "1 или более"),
    (r"a?", "0 или 1"),
    (r"a{2}", "Ровно 2"),
    (r"a{2,}", "2 или более"),
    (r"a{2,4}", "От 2 до 4"),
]

print(f"\nТекст: '{text}'")
for pattern, desc in quantifiers:
    matches = re.findall(pattern, text)
    print(f"  {pattern:<10} ({desc:15}) → {matches}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. СКОБКИ И ГРУППЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. СКОБКИ И ГРУППЫ")
print("─" * 70)

# Захватывающие группы
text = "2026-04-01"
match = re.match(r"(\d{4})-(\d{2})-(\d{2})", text)
if match:
    print(f"\nПолное совпадение: {match.group(0)}")
    print(f"Год: {match.group(1)}")
    print(f"Месяц: {match.group(2)}")
    print(f"День: {match.group(3)}")
    print(f"Все группы: {match.groups()}")

# Именованные группы
match = re.match(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", text)
if match:
    print(f"\nИменованные группы:")
    print(
        f"  year={match.group('year')}, month={match.group('month')}, day={match.group('day')}"
    )

# Не захватывающие группы
text = "file1.txt file2.log file3.txt"
files = re.findall(r"file\d+\.(?:txt|log)", text)
print(f"\nНе захватывающая группа: {files}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. НАБОРЫ СИМВОЛОВ [ ]
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. НАБОРЫ СИМВОЛОВ [ ]")
print("─" * 70)

text = "abc123XYZ!@#"

sets = [
    (r"[abc]", "a, b или c"),
    (r"[a-z]", "Строчная буква"),
    (r"[A-Z]", "Заглавная буква"),
    (r"[0-9]", "Цифра"),
    (r"[a-zA-Z]", "Любая буква"),
    (r"[^0-9]", "Не цифра"),
    (r"[abc123]", "a, b, c, 1, 2 или 3"),
]

print(f"\nТекст: '{text}'")
for pattern, desc in sets:
    matches = re.findall(pattern, text)
    print(f"  {pattern:<12} ({desc:20}) → {matches}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. ЖАДНОЕ И ЛЕНИВОЕ СОВПАДЕНИЕ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. ЖАДНОЕ И ЛЕНИВОЕ СОВПАДЕНИЕ")
print("─" * 70)

text = "<div>first</div><div>second</div>"

greedy = re.findall(r"<div>.*</div>", text)
lazy = re.findall(r"<div>.*?</div>", text)

print(f"\nТекст: '{text}'")
print(f"Жадное (.*):   {greedy}")
print(f"Ленивое (.*?): {lazy}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. ФЛАГИ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. ФЛАГИ")
print("─" * 70)

text = "HELLO\nWorld\nhello"

flags = [
    (re.IGNORECASE, "re.IGNORECASE (re.I)", r"hello"),
    (re.MULTILINE, "re.MULTILINE (re.M)", r"^\w+"),
    (re.DOTALL, "re.DOTALL (re.S)", r"HELLO.*hello"),
]

for flag, desc, pattern in flags:
    matches = re.findall(pattern, text, flag)
    print(f"\n{desc}:")
    print(f"  pattern: {pattern}")
    print(f"  result: {matches}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. СКОМПИЛИРОВАННЫЕ РЕГУЛЯРКИ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. СКОМПИЛИРОВАННЫЕ РЕГУЛЯРКИ")
print("─" * 70)

# Компиляция для повторного использования
email_pattern = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")

texts = ["Contact: alice@gmail.com", "Email bob.smith@company.org", "No email here"]

for text in texts:
    match = email_pattern.search(text)
    if match:
        print(f"  '{text}' → {match.group()}")
    else:
        print(f"  '{text}' → не найдено")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 9. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 9. ПРАКТИЧЕСКИЕ ПРИМЕРЫ")
print("─" * 70)


# 1. Валидация email
def is_valid_email(email):
    pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"
    return bool(re.match(pattern, email))


print("\nEmail валидация:")
for email in ["test@example.com", "invalid", "user@domain.org", "@bad.com"]:
    print(f"  {email:20} → {is_valid_email(email)}")

# 2. Извлечение телефонных номеров
text = "Тел: +7-999-123-45-67, +7 (999) 123 45 67, 89991234567"
phones = re.findall(
    r"(?:\+7|8)[\s\-\(\)]*\d{3}[\s\-\(\)]*\d{3}[\s\-\(\)]*\d{2}[\s\-\(\)]*\d{2}", text
)
print(f"\nТелефоны: {phones}")

# 3. Извлечение URL
text = "Visit https://example.com or http://test.org/path?q=1"
urls = re.findall(r"https?://\S+", text)
print(f"\nURL: {urls}")

# 4. Парсинг HTML тегов
html = "<h1>Заголовок</h1><p>Текст</p>"
tags = re.findall(r"<(\w+)>(.*?)</\1>", html)
print(f"\nHTML теги: {tags}")

# 5. Удаление лишних пробелов
text = "  hello    world   this   is   python  "
cleaned = re.sub(r"\s+", " ", text.strip())
print(f"\nУдаление пробелов: '{cleaned}'")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# ФУНКЦИИ
re.search(pattern, text)    # Первое совпадение
re.match(pattern, text)     # Только в начале
re.findall(pattern, text)   # Все совпадения (список)
re.finditer(pattern, text)  # Итератор Match
re.sub(pattern, repl, text) # Замена
re.split(pattern, text)     # Разбиение

# МЕТАСИМВОЛЫ
.  \d  \D  \w  \W  \s  \S
^  $  \b  \B

# КВАНТИФИКАТОРЫ
*  +  ?  {n}  {n,}  {n,m}
*? +? ??  — ленивые

# ГРУППЫ
(...)         — захватывающая
(?:...)       — не захватывающая
(?P<name>...) — именованная
[...]         — набор символов
[^...]        — отрицание набора
a|b           — a или b

# ФЛАГИ
re.IGNORECASE (re.I)
re.MULTILINE  (re.M)
re.DOTALL     (re.S)
re.VERBOSE    (re.X)
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
