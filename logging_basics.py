"""
╔══════════════════════════════════════════════════════════════════════╗
║            ШПАРГАЛКА ПО ЛОГИРОВАНИЮ В PYTHON                         ║
║                    logging — полный справочник                       ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import logging
import os
import tempfile

print("=" * 70)
print("📚 ШПАРГАЛКА ПО ЛОГИРОВАНИЮ")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. УРОВНИ ЛОГИРОВАНИЯ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. УРОВНИ ЛОГИРОВАНИЯ")
print("─" * 70)

levels = [
    (logging.DEBUG, "DEBUG", "Отладочная информация"),
    (logging.INFO, "INFO", "Общая информация"),
    (logging.WARNING, "WARNING", "Предупреждение"),
    (logging.ERROR, "ERROR", "Ошибка"),
    (logging.CRITICAL, "CRITICAL", "Критическая ошибка"),
]

print(f"\n{'Уровень':<12} {'Число':<8} {'Описание'}")
print("-" * 50)
for num, name, desc in levels:
    print(f"{name:<12} {num:<8} {desc}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. БАЗОВОЕ ИСПОЛЬЗОВАНИЕ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. БАЗОВОЕ ИСПОЛЬЗОВАНИЕ")
print("─" * 70)

# basicConfig — быстрый старт
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

logger.debug("Отладочное сообщение")
logger.info("Информационное сообщение")
logger.warning("Предупреждение")
logger.error("Ошибка")
logger.critical("Критическая ошибка")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. ФОРМАТИРОВАНИЕ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. ФОРМАТИРОВАНИЕ")
print("─" * 70)

formats = [
    ("%(asctime)s - %(levelname)s - %(message)s", "Стандарт"),
    ("%(name)s [%(lineno)d]: %(message)s", "Имя + строка"),
    ("%(levelname)-8s %(message)s", "Выровненный уровень"),
    ("%(threadName)s: %(message)s", "Поток"),
]

print(f"\n{'Атрибут':<20} {'Описание'}")
print("-" * 50)
attrs = [
    ("%(asctime)s", "Время"),
    ("%(name)s", "Имя логгера"),
    ("%(levelname)s", "Уровень (текст)"),
    ("%(levelno)s", "Уровень (число)"),
    ("%(message)s", "Сообщение"),
    ("%(filename)s", "Имя файла"),
    ("%(lineno)d", "Номер строки"),
    ("%(funcName)s", "Имя функции"),
    ("%(module)s", "Модуль"),
    ("%(threadName)s", "Имя потока"),
    ("%(process)d", "PID"),
]
for attr, desc in attrs:
    print(f"{attr:<20} {desc}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. HANDLERS (ОБРАБОТЧИКИ)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. HANDLERS")
print("─" * 70)

# Создаём логгер с несколькими handlers
logger2 = logging.getLogger("multi_handler")
logger2.setLevel(logging.DEBUG)

# Временный файл для примера
log_file = os.path.join(tempfile.gettempdir(), "example.log")

# File handler
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Stream handler (console)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)

# Формат
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger2.addHandler(file_handler)
logger2.addHandler(stream_handler)

logger2.debug("Это уйдёт только в файл")
logger2.warning("Это уйдёт и в файл, и в консоль")

print(f"\nЛог записан в: {log_file}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. ИЕРАРХИЯ ЛОГГЕРОВ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. ИЕРАРХИЯ ЛОГГЕРОВ")
print("─" * 70)

# Логгеры организованы по иерархии
root = logging.getLogger()
app = logging.getLogger("app")
app_db = logging.getLogger("app.db")
app_api = logging.getLogger("app.api")

print(f"\nroot logger: {root.name}")
print(f"app logger: {app.name}")
print(f"app.db logger: {app_db.name}")
print(f"app.api logger: {app_api.name}")
print(f"app_db.parent: {app_db.parent.name}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. КОНФИГУРАЦИЯ ЧЕРЕЗ DICT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. КОНФИГУРАЦИЯ ЧЕРЕЗ DICT")
print("─" * 70)

import logging.config

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        "detailed": {
            "format": "%(asctime)s [%(levelname)s] %(name)s:%(funcName)s:%(lineno)d: %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "app.log",
            "level": "DEBUG",
            "formatter": "detailed",
        },
    },
    "loggers": {
        "app": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

print("Конфигурация dictConfig:")
print(f"  Форматтеры: {list(log_config['formatters'].keys())}")
print(f"  Handlers: {list(log_config['handlers'].keys())}")
print(f"  Логгеры: {list(log_config['loggers'].keys())}")

# logging.config.dictConfig(log_config)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. LOGGING EXCEPTIONS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. ЛОГИРОВАНИЕ ИСКЛЮЧЕНИЙ")
print("─" * 70)

print("""
# logger.exception — автоматически добавляет traceback
try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("Ошибка деления")

# logger.error с exc_info
try:
    result = 10 / 0
except ZeroDivisionError:
    logger.error("Ошибка деления", exc_info=True)

# Оба выведут:
# ERROR:app:Ошибка деления
# Traceback (most recent call last):
#   File "app.py", line 10, in <module>
#     result = 10 / 0
# ZeroDivisionError: division by zero
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. ROTATING FILE HANDLER
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. РОТАЦИЯ ЛОГОВ")
print("─" * 70)

print("""
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# Ротация по размеру
handler = RotatingFileHandler(
    "app.log",
    maxBytes=10*1024*1024,  # 10 MB
    backupCount=5,
    encoding="utf-8",
)

# Ротация по времени
handler = TimedRotatingFileHandler(
    "app.log",
    when="midnight",
    interval=1,
    backupCount=7,
    encoding="utf-8",
)
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 9. ПРАКТИЧЕСКИЙ ПРИМЕР
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 9. ПРАКТИЧЕСКИЙ ПРИМЕР")
print("─" * 70)

print("""
# setup_logging.py
import logging
import logging.handlers

def setup_logging(log_file="app.log"):
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)-8s] %(name)s:%(lineno)d: %(message)s"
    )

    # Console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)

    # File с ротацией
    file_handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=10*1024*1024, backupCount=5, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Использование
logger = setup_logging()
logger.info("Приложение запущено")
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# БЫСТРЫЙ СТАРТ
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# УРОВНИ
logger.debug("Отладка")
logger.info("Инфо")
logger.warning("Предупреждение")
logger.error("Ошибка")
logger.critical("Критическая")

# ИСКЛЮЧЕНИЯ
try:
    ...
except Exception:
    logger.exception("Ошибка")

# HANDLERS
handler = logging.FileHandler("app.log")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# РОТАЦИЯ
RotatingFileHandler("app.log", maxBytes=10MB, backupCount=5)
TimedRotatingFileHandler("app.log", when="midnight")
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
