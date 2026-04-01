"""
╔══════════════════════════════════════════════════════════════════════╗
║            ШПАРГАЛКА ПО PYTEST В PYTHON                              ║
║         Фикстуры, параметризация, моки, маркеры                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""

print("=" * 70)
print("📚 ШПАРГАЛКА ПО PYTEST")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. БАЗОВЫЕ ТЕСТЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. БАЗОВЫЕ ТЕСТЫ")
print("─" * 70)


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b


print("\nПримеры тестов (в test_*.py):")
print("""
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. ASSERT СООБЩЕНИЯ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. ASSERT")
print("─" * 70)

print("""
# pytest показывает детальную информацию при провале
assert 1 + 1 == 2
assert "hello".upper() == "HELLO"
assert [1, 2, 3] == list(range(1, 4))
assert isinstance(42, int)
assert 3.14 == pytest.approx(3.14, abs=0.01)

# С сообщением (редко нужно — pytest и так покажет)
assert x > 0, f"x должен быть положительным, получил {x}"
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. ПРОВЕРКА ИСКЛЮЧЕНИЙ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. ПРОВЕРКА ИСКЛЮЧЕНИЙ")
print("─" * 70)

print("""
import pytest

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Деление на ноль"):
        divide(10, 0)

# Проверка деталей исключения
def test_exception_details():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert "Деление на ноль" in str(exc_info.value)
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. ФИКСТУРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. ФИКСТУРЫ")
print("─" * 70)

print("""
import pytest

# Простая фикстура
@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}

# С teardown (yield)
@pytest.fixture
def db_connection():
    conn = setup_database()
    yield conn
    conn.close()

# Scope: function, class, module, session
@pytest.fixture(scope="session")
def app():
    return create_app()

# Использование
def test_user(sample_data):
    assert sample_data["name"] == "Alice"

# Фикстура с параметрами
@pytest.fixture(params=["Alice", "Bob", "Charlie"])
def user_name(request):
    return request.param

def test_greet(user_name):
    assert greet(user_name).startswith("Привет")
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. ПАРАМЕТРИЗАЦИЯ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. ПАРАМЕТРИЗАЦИЯ")
print("─" * 70)

print("""
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# Несколько параметризаторов
@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [10, 20])
def test_combinations(x, y):
    pass  # 6 комбинаций: (1,10), (1,20), (2,10), ...

# Параметризация с ids
@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"),
    ("", ""),
], ids=["normal", "empty"])
def test_upper(input, expected):
    assert input.upper() == expected
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. МАРКЕРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. МАРКЕРЫ")
print("─" * 70)

print("""
@pytest.mark.slow
def test_big_computation():
    pass

@pytest.mark.skip(reason="Ещё не реализовано")
def test_future():
    pass

@pytest.mark.skipif(sys.platform == "win32", reason="Не для Windows")
def test_unix_only():
    pass

@pytest.mark.xfail
def test_known_bug():
    pass

# Запуск:
# pytest -m slow          # Только slow
# pytest -m "not slow"    # Кроме slow
# pytest -v               # Подробный вывод
# pytest -x               # Стоп при первой ошибке
# pytest --tb=short       # Короткий traceback
# pytest -k "add"         # Только тесты с "add" в имени
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. МОКИ (unittest.mock)
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. МОКИ")
print("─" * 70)

print("""
from unittest.mock import Mock, patch

# Mock объект
def test_mock():
    mock = Mock(return_value=42)
    assert mock() == 42
    mock.assert_called_once()

# patch — подмена функции/класса
@patch("requests.get")
def test_api(mock_get):
    mock_get.return_value.json.return_value = {"id": 1}
    result = fetch_user(1)
    assert result["id"] == 1
    mock_get.assert_called_once_with("https://api.example.com/users/1")

# patch как контекстный менеджер
def test_with_context():
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True
        assert process_file("test.txt") == "ok"

# patch.object
def test_patch_object():
    obj = MyClass()
    with patch.object(obj, "method", return_value=42):
        assert obj.method() == 42
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. CONFTEST.PY
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. CONFTEST.PY")
print("─" * 70)

print("""
# conftest.py — общие фикстуры для всех тестов
# Автоматически обнаруживается pytest

import pytest

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()

# Фикстуры из conftest доступны во всех test_*.py
# в той же директории и вложенных

# Структура проекта:
# tests/
#   conftest.py        # Общие фикстуры
#   test_api.py        # Тесты API
#   test_models/
#     conftest.py      # Фикстуры для models
#     test_user.py
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 9. ПРАКТИЧЕСКИЙ ПРИМЕР
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 9. ПРАКТИЧЕСКИЙ ПРИМЕР")
print("─" * 70)

print("""
# test_calculator.py
import pytest

class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль")
        return a / b

@pytest.fixture
def calc():
    return Calculator()

class TestCalculator:
    def test_add(self, calc):
        assert calc.add(2, 3) == 5

    @pytest.mark.parametrize("a,b,expected", [
        (10, 2, 5.0),
        (7, 2, 3.5),
        (0, 1, 0.0),
    ])
    def test_divide(self, calc, a, b, expected):
        assert calc.divide(a, b) == expected

    def test_divide_by_zero(self, calc):
        with pytest.raises(ValueError):
            calc.divide(10, 0)
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# ЗАПУСК
pytest                    # Все тесты
pytest test_file.py       # Конкретный файл
pytest -v                 # Подробно
pytest -x                 # Стоп при ошибке
pytest -k "add"           # По имени
pytest -m slow            # По маркеру
pytest --tb=short         # Короткий traceback
pytest --cov=module       # Покрытие

# ФИКСТУРЫ
@pytest.fixture
def data():
    return {"a": 1}

@pytest.fixture(scope="session")
def app(): ...

# ПАРАМЕТРИЗАЦИЯ
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# МОКИ
@patch("module.func")
def test(mock_func):
    mock_func.return_value = 42

# ИСКЛЮЧЕНИЯ
with pytest.raises(ValueError, match="msg"):
    func()
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
