"""
╔══════════════════════════════════════════════════════════════════════╗
║            ШПАРГАЛКА ПО ASYNCIO В PYTHON                             ║
║              async/await, задачи, очереди, пулы                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import time

print("=" * 70)
print("📚 ШПАРГАЛКА ПО ASYNCIO")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# 🔹 1. ОСНОВЫ ASYNC/AWAIT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 1. ОСНОВЫ ASYNC/AWAIT")
print("─" * 70)


async def greet(name):
    print(f"  Привет, {name}!")
    await asyncio.sleep(0.1)
    return f"Готово: {name}"


# Запуск через asyncio.run()
result = asyncio.run(greet("Алиса"))
print(f"\nРезультат: {result}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 2. ЗАПУСК НЕСКОЛЬКИХ КОРУТИН
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 2. GATHER — ПАРАЛЛЕЛЬНЫЙ ЗАПУСК")
print("─" * 70)


async def task(name, delay):
    print(f"  [{name}] начало")
    await asyncio.sleep(delay)
    print(f"  [{name}] завершение")
    return f"{name}: {delay}с"


async def run_gather():
    results = await asyncio.gather(
        task("A", 0.1),
        task("B", 0.2),
        task("C", 0.15),
    )
    return results


results = asyncio.run(run_gather())
print(f"\nРезультаты: {results}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 3. TASK — УПРАВЛЕНИЕ ЗАДАЧАМИ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 3. TASK — УПРАВЛЕНИЕ ЗАДАЧАМИ")
print("─" * 70)


async def run_tasks():
    task1 = asyncio.create_task(task("X", 0.1))
    task2 = asyncio.create_task(task("Y", 0.2))

    await asyncio.sleep(0.05)
    print(f"  task1.done(): {task1.done()}")

    results = await asyncio.gather(task1, task2)
    return results


results = asyncio.run(run_tasks())
print(f"\nРезультаты: {results}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 4. TIMEOUT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 4. TIMEOUT")
print("─" * 70)


async def slow_operation():
    await asyncio.sleep(10)
    return "Готово"


async def run_timeout():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=0.2)
        return result
    except asyncio.TimeoutError:
        return "Таймаут!"


result = asyncio.run(run_timeout())
print(f"\nРезультат: {result}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 5. WAIT_FOR И GATHER VS WAIT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 5. WAIT — ОЖИДАНИЕ НЕСКОЛЬКИХ")
print("─" * 70)


async def run_wait():
    t1 = asyncio.create_task(task("1", 0.1))
    t2 = asyncio.create_task(task("2", 0.3))
    t3 = asyncio.create_task(task("3", 0.2))

    done, pending = await asyncio.wait(
        {t1, t2, t3},
        timeout=0.25,
    )

    print(f"  Завершено: {len(done)}, Ожидает: {len(pending)}")

    # Отмена оставшихся
    for t in pending:
        t.cancel()

    return [t.result() for t in done]


results = asyncio.run(run_wait())
print(f"Результаты: {results}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 6. ASYNCIO.QUEUE — ОЧЕРЕДЬ
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 6. ОЧЕРЕДЬ (Queue)")
print("─" * 70)


async def worker(queue, worker_id):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"  Worker {worker_id} обработал: {item}")
        await asyncio.sleep(0.05)
        queue.task_done()


async def run_queue():
    queue = asyncio.Queue()

    # Добавляем задачи
    for i in range(5):
        await queue.put(i)

    # Запускаем воркеров
    workers = [asyncio.create_task(worker(queue, i)) for i in range(2)]

    # Ждём обработки
    await queue.join()

    # Останавливаем воркеров
    for w in workers:
        await queue.put(None)

    await asyncio.gather(*workers)
    print("  Все задачи обработаны!")


asyncio.run(run_queue())

# ═══════════════════════════════════════════════════════════════════════
# 🔹 7. СИНХРОННЫЙ КОД В ASYNC
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 7. СИНХРОННЫЙ КОД В ASYNC")
print("─" * 70)


def blocking_io():
    time.sleep(0.1)
    return "IO завершён"


async def run_in_executor():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, blocking_io)
    return result


result = asyncio.run(run_in_executor())
print(f"\nРезультат: {result}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 8. ПРАКТИЧЕСКИЙ ПРИМЕР: ВЕБ-СКРЕЙПЕР
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "─" * 70)
print("🔹 8. ПРАКТИЧЕСКИЙ ПРИМЕР: АСИНХРОННЫЙ ПАТТЕРН")
print("─" * 70)


async def fetch_url(url, delay):
    print(f"  Загрузка {url}...")
    await asyncio.sleep(delay)
    return f"Данные с {url}"


async def fetch_all(urls):
    tasks = [fetch_url(url, 0.1) for url in urls]
    return await asyncio.gather(*tasks)


urls = ["http://example.com/1", "http://example.com/2", "http://example.com/3"]
results = asyncio.run(fetch_all(urls))
print(f"\nРезультаты: {results}")

# ═══════════════════════════════════════════════════════════════════════
# 🔹 БЫСТРЫЙ СПРАВОЧНИК
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("🚀 БЫСТРЫЙ СПРАВОЧНИК")
print("=" * 70)

quick_ref = """
# ОСНОВЫ
async def func():
    await asyncio.sleep(1)
    return result

asyncio.run(func())

# ПАРАЛЛЕЛЬНЫЙ ЗАПУСК
await asyncio.gather(task1(), task2())

# TASK
task = asyncio.create_task(func())
await task
task.cancel()
task.done()

# TIMEOUT
await asyncio.wait_for(func(), timeout=5.0)

# WAIT
done, pending = await asyncio.wait({t1, t2})

# QUEUE
queue = asyncio.Queue()
await queue.put(item)
item = await queue.get()
queue.task_done()
await queue.join()

# СИНХРОННЫЙ КОД
loop = asyncio.get_running_loop()
await loop.run_in_executor(None, blocking_func)
"""
print(quick_ref)
print("=" * 70)
print("✅ Шпаргалка завершена!")
print("=" * 70)
