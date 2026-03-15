"""
╔══════════════════════════════════════════════════════════════════════╗
║                    ШПАРГАЛКА ПО DATETIME В PYTHON                    ║
║                        Полный справочник                             ║
╚══════════════════════════════════════════════════════════════════════╝

📅 Основные классы:
   • date      — только дата
   • time      — только время  
   • datetime  — дата + время
   • timedelta — разница между датами
   • timezone  — часовой пояс
"""

# ═══════════════════════════════════════════════════════════════════════
# 🔹 ИМПОРТЫ
# ═══════════════════════════════════════════════════════════════════════

from datetime import date, time, datetime, timedelta, timezone
import calendar

print("=" * 70)
print("📚 ШПАРГАЛКА ПО DATETIME В PYTHON")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. СОЗДАНИЕ ОБЪЕКТОВ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. СОЗДАНИЕ ОБЪЕКТОВ")
print("─" * 70)

# Текущая дата и время
now = datetime.now()
print(f"datetime.now():          {now}")

today = date.today()
print(f"date.today():            {today}")

# UTC время (рекомендуемый способ)
utc_now = datetime.now(timezone.utc)
print(f"datetime.now(timezone.utc): {utc_now}")

# Создание вручную
d = date(2026, 2, 11)
print(f"\ndate(2026, 2, 11):       {d}")

t = time(14, 30, 45, 123456)
print(f"time(14, 30, 45, 123456): {t}")

dt = datetime(2026, 2, 11, 14, 30, 45)
print(f"datetime(2026, 2, 11, 14, 30, 45): {dt}")

# С часовым поясом
dt_msk = datetime(2026, 2, 11, 14, 30, tzinfo=timezone(timedelta(hours=3)))
print(f"datetime с часовым поясом (МСК): {dt_msk}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. АТРИБУТЫ И МЕТОДЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. АТРИБУТЫ И МЕТОДЫ")
print("─" * 70)

dt = datetime.now()
print(f"\ndt.year:         {dt.year}")
print(f"dt.month:        {dt.month}")
print(f"dt.day:          {dt.day}")
print(f"dt.hour:         {dt.hour}")
print(f"dt.minute:       {dt.minute}")
print(f"dt.second:       {dt.second}")
print(f"dt.microsecond:  {dt.microsecond}")
print(f"dt.weekday():    {dt.weekday()}    # Пн=0, Вс=6")
print(f"dt.isoweekday(): {dt.isoweekday()}   # Пн=1, Вс=7")
print(f"dt.date():       {dt.date()}       # Только дата")
print(f"dt.time():       {dt.time()}       # Только время")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. TIMEDATE - АРИФМЕТИКА ДАТ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. TIMEDATE - АРИФМЕТИКА ДАТ")
print("─" * 70)

today = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
next_week = today + timedelta(weeks=1)
three_days_ago = today - timedelta(days=3)

print(f"\nСегодня:          {today}")
print(f"Завтра:           {tomorrow}")
print(f"Вчера:            {yesterday}")
print(f"Через неделю:     {next_week}")
print(f"3 дня назад:      {three_days_ago}")

# С временем
now = datetime.now()
hour_later = now + timedelta(hours=1)
two_hours_ago = now - timedelta(hours=2)
minutes_added = now + timedelta(minutes=30)

print(f"\nСейчас:           {now.strftime('%H:%M:%S')}")
print(f"Через час:        {hour_later.strftime('%H:%M:%S')}")
print(f"2 часа назад:     {two_hours_ago.strftime('%H:%M:%S')}")
print(f"+30 минут:        {minutes_added.strftime('%H:%M:%S')}")

# Разница между датами
date1 = datetime(2026, 12, 31)
date2 = datetime(2026, 1, 1)
delta = date1 - date2
print(f"\nРазница между 01.01.2026 и 31.12.2026: {delta}")
print(f"Дней: {delta.days}")
print(f"Секунд: {delta.total_seconds():,.0f}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. ФОРМАТИРОВАНИЕ (STRFTIME)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. ФОРМАТИРОВАНИЕ (strftime)")
print("─" * 70)

now = datetime.now()

formats = {
    "%d.%m.%Y": "ДД.ММ.ГГГГ",
    "%Y-%m-%d": "ГГГГ-ММ-ДД",
    "%Y-%m-%d %H:%M:%S": "Полный формат",
    "%A, %d %B %Y": "Полное название дня и месяца",
    "%H:%M:%S": "Только время",
    "%I:%M %p": "12-часовой формат",
    "%d/%m/%y": "ДД/ММ/ГГ",
    "%B %Y": "Месяц Год",
    "%a %b %d %H:%M:%S %Y": "Unix-стиль",
    "%Y%m%d_%H%M%S": "Для имён файлов",
}

print("\nПримеры форматирования текущего времени:\n")
for fmt, desc in formats.items():
    print(f"{desc:30} | {fmt:30} → {now.strftime(fmt)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. ПАРСИНГ СТРОКИ В ДАТУ (STRPTIME)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. ПАРСИНГ СТРОКИ В ДАТУ (strptime)")
print("─" * 70)

examples = [
    ("11.02.2026", "%d.%m.%Y"),
    ("2026-02-11", "%Y-%m-%d"),
    ("2026-02-11 14:30:45", "%Y-%m-%d %H:%M:%S"),
    ("11/Feb/2026", "%d/%b/%Y"),
    ("Wednesday, 11 February 2026", "%A, %d %B %Y"),
    ("11.02.26", "%d.%m.%y"),
    ("14:30:45", "%H:%M:%S"),
    ("02/11/2026 14:30", "%m/%d/%Y %H:%M"),
]

print("\n")
for string, fmt in examples:
    try:
        parsed = datetime.strptime(string, fmt)
        print(f"{string:30} | {fmt:25} → {parsed}")
    except ValueError as e:
        print(f"{string:30} | {fmt:25} → ОШИБКА: {e}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. РАБОТА С ЧАСОВЫМИ ПОЯСАМИ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. РАБОТА С ЧАСОВЫМИ ПОЯСАМИ")
print("─" * 70)

# UTC время
utc_dt = datetime.now(timezone.utc)
print(f"\nUTC время: {utc_dt}")

# Москва (UTC+3)
msk_tz = timezone(timedelta(hours=3))
msk_dt = utc_dt.astimezone(msk_tz)
print(f"Москва (UTC+3): {msk_dt}")

# Нью-Йорк (UTC-5)
ny_tz = timezone(timedelta(hours=-5))
ny_dt = utc_dt.astimezone(ny_tz)
print(f"Нью-Йорк (UTC-5): {ny_dt}")

# Преобразование между поясами
dt_utc = datetime(2026, 2, 11, 11, 0, tzinfo=timezone.utc)
dt_msk = dt_utc.astimezone(timezone(timedelta(hours=3)))
print(f"\n11:00 UTC = {dt_msk.strftime('%H:%M')} MSK")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. ПОЛЕЗНЫЕ МЕТОДЫ И ПРИМЕРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. ПОЛЕЗНЫЕ МЕТОДЫ И ПРИМЕРЫ")
print("─" * 70)

# ISO формат
now = datetime.now()
iso_str = now.isoformat()
print(f"\nISO формат: {iso_str}")

# Обратное преобразование (Python 3.7+)
iso_date = date.fromisoformat("2026-02-11")
print(f"fromisoformat: {iso_date}")

# Первый и последний день месяца
year, month = 2026, 2
first_day = date(year, month, 1)
_, days_in_month = calendar.monthrange(year, month)
last_day = date(year, month, days_in_month)

print(f"\nПервый день февраля 2026: {first_day}")
print(f"Последний день февраля 2026: {last_day}")

# Високосный год
print(f"\n2024 - високосный год? {calendar.isleap(2024)}")
print(f"2026 - високосный год? {calendar.isleap(2026)}")

# Количество дней в месяце
print(f"\nДней в феврале 2024: {calendar.monthrange(2024, 2)[1]}")
print(f"Дней в феврале 2026: {calendar.monthrange(2026, 2)[1]}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. ПРАКТИЧЕСКИЕ ПРИМЕРЫ")
print("─" * 70)

# Пример 1: Возраст человека
print("\n1️⃣  Расчет возраста:")
birthday = date(1990, 5, 15)
today = date.today()
age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
print(f"   Дата рождения: {birthday}")
print(f"   Возраст: {age} лет")

# Пример 2: Дней до Нового года
print("\n2️⃣  Дней до Нового года:")
new_year = date(today.year + 1, 1, 1)
days_left = (new_year - today).days
print(f"   Сегодня: {today}")
print(f"   Новый год: {new_year}")
print(f"   Осталось дней: {days_left}")

# Пример 3: Время выполнения операции
print("\n3️⃣  Замер времени выполнения:")
import time as time_module
start = datetime.now()
time_module.sleep(0.5)  # имитация работы
end = datetime.now()
duration = end - start
print(f"   Время выполнения: {duration.total_seconds():.3f} сек")

# Пример 4: Проверка, рабочий ли день
print("\n4️⃣  Проверка рабочего дня:")
def is_weekday(d):
    return d.weekday() < 5  # Пн-Пт = 0-4

test_dates = [
    date(2026, 2, 10),  # Вторник
    date(2026, 2, 14),  # Суббота
    date(2026, 2, 15),  # Воскресенье
]

for d in test_dates:
    day_name = d.strftime("%A")
    status = "✅ Рабочий" if is_weekday(d) else "❌ Выходной"
    print(f"   {d} ({day_name}): {status}")

# Пример 5: Генерация диапазона дат
print("\n5️⃣  Генерация диапазона дат (следующие 7 дней):")
start_date = date.today()
for i in range(7):
    current_date = start_date + timedelta(days=i)
    print(f"   {current_date.strftime('%d.%m.%Y')} ({current_date.strftime('%A')})")

# Пример 6: Нахождение следующего понедельника
print("\n6️⃣  Следующий понедельник:")
today = date.today()
days_until_monday = (7 - today.weekday()) % 7
if days_until_monday == 0:
    days_until_monday = 7
next_monday = today + timedelta(days=days_until_monday)
print(f"   Сегодня: {today} ({today.strftime('%A')})")
print(f"   Следующий понедельник: {next_monday}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 9. СПРАВОЧНИК ФОРМАТОВ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 9. СПРАВОЧНИК ФОРМАТОВ strftime/strptime")
print("─" * 70)

format_codes = [
    ("%Y", "Год (4 цифры)", "2026"),
    ("%y", "Год (2 цифры)", "26"),
    ("%m", "Месяц (01-12)", "02"),
    ("%B", "Название месяца", "February"),
    ("%b", "Сокращенное название", "Feb"),
    ("%d", "День месяца (01-31)", "11"),
    ("%A", "Название дня недели", "Wednesday"),
    ("%a", "Сокращенное название", "Wed"),
    ("%H", "Часы (00-23)", "14"),
    ("%I", "Часы (01-12)", "02"),
    ("%p", "AM/PM", "PM"),
    ("%M", "Минуты (00-59)", "30"),
    ("%S", "Секунды (00-59)", "45"),
    ("%f", "Микросекунды", "123456"),
    ("%z", "Смещение UTC", "+0300"),
    ("%Z", "Название часового пояса", "MSK"),
    ("%%", "Символ %", "%"),
]

print("\n{:<10} {:<30} {:<15}".format("Код", "Описание", "Пример"))
print("-" * 70)
for code, desc, example in format_codes:
    print("{:<10} {:<30} {:<15}".format(code, desc, example))

# ═══════════════════════════════════════════════════════════════════════
# 🔹 10. ВАЖНЫЕ ЗАМЕЧАНИЯ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 10. ВАЖНЫЕ ЗАМЕЧАНИЯ")
print("─" * 70)

notes = [
    "⚠️  datetime.now() - локальное время, datetime.utcnow() - UTC (устаревшее)",
    "⚠️  Для UTC используйте: datetime.now(timezone.utc)",
    "⚠️  Сравнивать можно только объекты одного типа (оба с tzinfo или оба без)",
    "⚠️  timedelta не поддерживает месяцы/годы (разная длина)",
    "💡 Для сложной работы с датами используйте: dateutil, pendulum, arrow",
    "💡 Для часовых поясов (страны/города): pytz или zoneinfo (Python 3.9+)",
]

print("\n")
for note in notes:
    print(f"   {note}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК ДЛЯ КОПИРОВАНИЯ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК ДЛЯ КОПИРОВАНИЯ")
print("=" * 70)

quick_reference = """
# Базовый импорт
from datetime import datetime, date, timedelta, timezone

# Текущее время
now = datetime.now()
today = date.today()

# Создание
dt = datetime(2026, 2, 11, 14, 30, 45)
d = date(2026, 2, 11)
t = time(14, 30, 45)

# Форматирование
now.strftime("%d.%m.%Y %H:%M:%S")  # '11.02.2026 14:30:45'

# Парсинг
datetime.strptime("11.02.2026", "%d.%m.%Y")

# Арифметика
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

# Разница
delta = date2 - date1
days = delta.days

# UTC время
utc_now = datetime.now(timezone.utc)

# ISO формат
iso_str = now.isoformat()
date_obj = date.fromisoformat("2026-02-11")
"""

print(quick_reference)

print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)