"""
╔══════════════════════════════════════════════════════════════════════╗
║          ШПАРГАЛКА ПО REQUESTS В PYTHON                              ║
║              HTTP-запросы, сессии, аутентификация                    ║
╚══════════════════════════════════════════════════════════════════════╝
"""

print("=" * 70)
print("📚 ШПАРГАЛКА ПО REQUESTS")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. БАЗОВЫЕ ЗАПРОСЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. БАЗОВЫЕ ЗАПРОСЫ")
print("─" * 70)

print("""
import requests

# GET
response = requests.get("https://api.example.com/users")

# POST
response = requests.post(
    "https://api.example.com/users",
    json={"name": "Alice", "age": 30}
)

# PUT
response = requests.put(
    "https://api.example.com/users/1",
    json={"name": "Alice Updated"}
)

# PATCH
response = requests.patch(
    "https://api.example.com/users/1",
    json={"age": 31}
)

# DELETE
response = requests.delete("https://api.example.com/users/1")
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. ОБЪЕКТ RESPONSE
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. ОБЪЕКТ RESPONSE")
print("─" * 70)

print("""
response = requests.get("https://api.example.com/users")

# Статус
response.status_code          # 200, 404, 500...
response.ok                   # True если 2xx
response.reason               # "OK", "Not Found"...

# Данные
response.json()               # JSON → dict/list
response.text                 # Текст (str)
response.content              # Байты (bytes)

# Заголовки
response.headers              # dict заголовков
response.headers["Content-Type"]

# Мета
response.url                  # Финальный URL (после редиректов)
response.elapsed              # Время ответа (timedelta)
response.cookies              # Cookies
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. ПАРАМЕТРЫ ЗАПРОСА
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. ПАРАМЕТРЫ ЗАПРОСА")
print("─" * 70)

print("""
# Query параметры
params = {"q": "python", "page": 1, "limit": 10}
response = requests.get("https://api.example.com/search", params=params)
# URL: https://api.example.com/search?q=python&page=1&limit=10

# Заголовки
headers = {
    "Authorization": "Bearer token123",
    "Accept": "application/json",
    "User-Agent": "MyApp/1.0",
}
response = requests.get(url, headers=headers)

# Тело запроса
# JSON
response = requests.post(url, json={"key": "value"})

# Form data
response = requests.post(url, data={"key": "value"})

# Файлы
with open("file.txt", "rb") as f:
    response = requests.post(url, files={"file": f})
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. ТАЙМАУТЫ И ПОВТОРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. ТАЙМАУТЫ И ПОВТОРЫ")
print("─" * 70)

print("""
# Таймаут (всегда указывайте!)
response = requests.get(url, timeout=5)
response = requests.get(url, timeout=(3.05, 10))  # (connect, read)

# Повторы с requests.adapters
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry)
session.mount("http://", adapter)
session.mount("https://", adapter)

response = session.get(url)
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. СЕССИИ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. СЕССИИ")
print("─" * 70)

print("""
# Session сохраняет cookies и переиспользует соединение
session = requests.Session()

# Общие заголовки для всех запросов
session.headers.update({"Authorization": "Bearer token"})

# Автоматическое сохранение cookies
session.get("https://example.com/login", data={"user": "admin"})
session.get("https://example.com/profile")  # cookie отправится автоматически

# Контекстный менеджер
with requests.Session() as session:
    session.get(url)
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. АУТЕНТИФИКАЦИЯ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. АУТЕНТИФИКАЦИЯ")
print("─" * 70)

print("""
# Basic Auth
response = requests.get(url, auth=("user", "pass"))

# Bearer Token
headers = {"Authorization": "Bearer <token>"}
response = requests.get(url, headers=headers)

# Custom Auth
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["X-Token"] = self.token
        return r

response = requests.get(url, auth=TokenAuth("my-token"))
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. ОБРАБОТКА ОШИБОК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. ОБРАБОТКА ОШИБОК")
print("─" * 70)

print("""
import requests

# Проверка статуса
response = requests.get(url)
response.raise_for_status()  # Raises HTTPError для 4xx/5xx

# Полный блок обработки
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.Timeout:
    print("Таймаут!")
except requests.exceptions.ConnectionError:
    print("Ошибка соединения!")
except requests.exceptions.HTTPError as e:
    print(f"HTTP ошибка: {e}")
except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")
except ValueError:
    print("Невалидный JSON!")
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. ПРАКТИЧЕСКИЕ ПРИМЕРЫ")
print("─" * 70)

print("""
# 1. Пагинация
def fetch_all_pages(base_url):
    page = 1
    all_data = []
    while True:
        response = requests.get(base_url, params={"page": page})
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        all_data.extend(data)
        page += 1
    return all_data

# 2. Скачивание файла
def download_file(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

# 3. API клиент
class APIClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        })

    def get(self, path, **kwargs):
        response = self.session.get(f"{self.base_url}/{path}", **kwargs)
        response.raise_for_status()
        return response.json()

    def post(self, path, **kwargs):
        response = self.session.post(f"{self.base_url}/{path}", **kwargs)
        response.raise_for_status()
        return response.json()
""")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# ЗАПРОСЫ
requests.get(url, params={}, headers={}, timeout=5)
requests.post(url, json={}, data={}, files={})
requests.put(url, json={})
requests.delete(url)

# RESPONSE
response.status_code, response.ok
response.json(), response.text, response.content
response.headers, response.cookies

# СЕССИЯ
session = requests.Session()
session.headers.update({"Auth": "Bearer token"})
session.get(url)

# ОШИБКИ
response.raise_for_status()
requests.exceptions.Timeout
requests.exceptions.ConnectionError
requests.exceptions.HTTPError

# КОДЫ СТАТУСОВ
200 OK, 201 Created
400 Bad Request, 401 Unauthorized
403 Forbidden, 404 Not Found
500 Server Error
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
