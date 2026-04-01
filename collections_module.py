"""
╔══════════════════════════════════════════════════════════════════════╗
║        ШПАРГАЛКА ПО МОДУЛЮ COLLECTIONS В PYTHON                      ║
║     Counter, defaultdict, namedtuple, deque, OrderedDict             ║
╚══════════════════════════════════════════════════════════════════════╝
"""

from collections import Counter, defaultdict, namedtuple, deque, OrderedDict, ChainMap

print("=" * 70)
print("📚 ШПАРГАЛКА ПО COLLECTIONS")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. COUNTER — ПОДСЧЁТ ЭЛЕМЕНТОВ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. COUNTER")
print("─" * 70)

# Создание
text = "hello world"
counter = Counter(text)
print(f"\nCounter('{text}'): {counter}")

# Из списка
fruits = ["яблоко", "банан", "яблоко", "вишня", "банан", "яблоко"]
fruit_counter = Counter(fruits)
print(f"Counter(fruits): {fruit_counter}")

# most_common()
print(f"\nmost_common(2): {fruit_counter.most_common(2)}")

# Операции
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(f"\nc1: {c1}")
print(f"c2: {c2}")
print(f"c1 + c2: {c1 + c2}")
print(f"c1 - c2: {c1 - c2}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. DEFAULTDICT — СЛОВАРЬ СО ЗНАЧЕНИЕМ ПО УМОЛЧАНИЮ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. DEFAULTDICT")
print("─" * 70)

# Группировка
words = ["apple", "banana", "avocado", "blueberry", "apricot"]
by_first = defaultdict(list)
for word in words:
    by_first[word[0]].append(word)

print(f"\nГруппировка по первой букве:")
for key, values in by_first.items():
    print(f"  {key}: {values}")

# Подсчёт
word = "programming"
char_count = defaultdict(int)
for char in word:
    char_count[char] += 1

print(f"\nПодсчёт символов: {dict(char_count)}")

# Вложенный defaultdict
tree = lambda: defaultdict(tree)
users = tree()
users["alice"]["age"] = 30
users["alice"]["city"] = "Москва"
users["bob"]["age"] = 25

print(f"\nВложенный defaultdict:")
print(f"  users['alice']: {dict(users['alice'])}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. NAMEDTUPLE — КОРТЕЖ С ИМЕНАМИ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. NAMEDTUPLE")
print("─" * 70)

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)

print(f"\nPoint: {p}")
print(f"p.x: {p.x}, p.y: {p.y}")
print(f"p[0]: {p[0]}, p[1]: {p[1]}")

# _asdict()
print(f"p._asdict(): {p._asdict()}")

# _replace()
p2 = p._replace(x=10)
print(f"p._replace(x=10): {p2}")

# Практический пример
User = namedtuple("User", ["name", "age", "email"])
users = [
    User("Alice", 30, "alice@example.com"),
    User("Bob", 25, "bob@example.com"),
]

print(f"\nСортировка по возрасту:")
for user in sorted(users, key=lambda u: u.age):
    print(f"  {user.name}: {user.age}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. DEQUE — ДВУСТОРОННЯЯ ОЧЕРЕДЬ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. DEQUE")
print("─" * 70)

dq = deque([1, 2, 3])
print(f"\ndeque: {dq}")

# Добавление
dq.append(4)  # В конец
dq.appendleft(0)  # В начало
print(f"После append(4), appendleft(0): {dq}")

# Удаление
right = dq.pop()
left = dq.popleft()
print(f"pop(): {right}, popleft(): {left}")
print(f"Осталось: {dq}")

# maxlen — ограниченная очередь
history = deque(maxlen=3)
for i in range(6):
    history.append(i)
print(f"\ndeque(maxlen=3) после 6 добавлений: {history}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. ORDEREDDICT — СЛОВАРЬ С ПОРЯДКОМ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. ORDEREDDICT")
print("─" * 70)

od = OrderedDict()
od["c"] = 3
od["a"] = 1
od["b"] = 2

print(f"\nOrderedDict: {od}")

# move_to_end
od.move_to_end("a")
print(f"move_to_end('a'): {od}")

od.move_to_end("c", last=False)
print(f"move_to_end('c', last=False): {od}")

# popitem
key, value = od.popitem(last=True)
print(f"popitem(): {key}={value}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. CHAINMAP — ОБЪЕДИНЕНИЕ СЛОВАРЕЙ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. CHAINMAP")
print("─" * 70)

defaults = {"theme": "dark", "lang": "en", "debug": False}
user_settings = {"theme": "light", "lang": "ru"}

config = ChainMap(user_settings, defaults)
print(f"\nconfig['theme']: {config['theme']}")  # user_settings
print(f"config['debug']: {config['debug']}")  # defaults
print(f"config.maps: {list(config.maps)}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. ПРАКТИЧЕСКИЕ ПРИМЕРЫ")
print("─" * 70)


# 1. Анаграммы
def are_anagrams(s1, s2):
    return Counter(s1.replace(" ", "").lower()) == Counter(s2.replace(" ", "").lower())


print(f"\nare_anagrams('listen', 'silent'): {are_anagrams('listen', 'silent')}")
print(f"are_anagrams('hello', 'world'): {are_anagrams('hello', 'world')}")


# 2. LRU Cache на deque
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


cache = LRUCache(3)
cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)
cache.put("d", 4)  # Вытесняет "a"
print(f"\nLRUCache.get('a'): {cache.get('a')}")
print(f"LRUCache.get('b'): {cache.get('b')}")


# 3. BFS с deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(graph.get(node, []))
    return order


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": [],
}
print(f"\nBFS от 'A': {bfs(graph, 'A')}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# COUNTER
Counter(iterable)           # Подсчёт
counter.most_common(n)      # Топ-n
c1 + c2, c1 - c2            # Операции

# DEFAULTDICT
dd = defaultdict(list)      # Значение по умолчанию
dd = defaultdict(int)       # 0 по умолчанию
dd = defaultdict(set)       # Пустое множество

# NAMEDTUPLE
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
p._asdict(), p._replace(x=10)

# DEQUE
dq = deque([1, 2, 3])
dq.append(x), dq.appendleft(x)
dq.pop(), dq.popleft()
dq = deque(maxlen=10)       # Ограниченная

# ORDEREDDICT
od.move_to_end(key, last=True)
od.popitem(last=True)

# CHAINMAP
cm = ChainMap(dict1, dict2)  # dict1 приоритетнее
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
