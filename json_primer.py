import json
import os

# 1. Чтение JSON из строки
def read_json_from_string():
    print("=== Чтение JSON из строки ===")
    json_string = '{"name": "Alice", "age": 25, "city": "New York"}'
    data = json.loads(json_string)
    print("Результат:", data)
    print("Тип данных:", type(data), "\n")


# 2. Чтение JSON из файла
def read_json_from_file(filename):
    print("=== Чтение JSON из файла ===")
    if not os.path.exists(filename):
        print(f"Файл {filename} не существует.")
        return

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    print("Результат:", data)
    print("Тип данных:", type(data), "\n")


# 3. Запись JSON в строку
def write_json_to_string():
    print("=== Запись JSON в строку ===")
    data = {
        "name": "Charlie",
        "age": 35,
        "city": "Chicago"
    }
    json_string = json.dumps(data, indent=4, ensure_ascii=False)
    print("JSON-строка:")
    print(json_string, "\n")


# 4. Запись JSON в файл
def write_json_to_file(filename):
    print("=== Запись JSON в файл ===")
    data = {
        "name": "David",
        "age": 40,
        "city": "San Francisco"
    }

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Данные успешно записаны в файл {filename}\n")


# 5. Обработка ошибок при работе с JSON
def handle_json_errors():
    print("=== Обработка ошибок JSON ===")
    invalid_json = '{"name": "Alice", "age": 25, "city": "New York"'  # Отсутствует закрывающая фигурная скобка

    try:
        data = json.loads(invalid_json)
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON: {e}")
    print()


# 6. Сериализация пользовательских объектов
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {"name": self.name, "age": self.age}


def serialize_custom_object():
    print("=== Сериализация пользовательского объекта ===")
    person = Person("Frank", 45)

    # Сериализация с использованием пользовательского метода
    json_string = json.dumps(person.to_dict(), indent=4)
    print("JSON-строка:")
    print(json_string, "\n")


# Основная функция для запуска всех примеров
def main():
    # Пример 1: Чтение JSON из строки
    read_json_from_string()

    # Пример 2: Чтение JSON из файла (создайте файл data.json заранее)
    read_json_from_file('data.json')

    # Пример 3: Запись JSON в строку
    write_json_to_string()

    # Пример 4: Запись JSON в файл
    write_json_to_file('output.json')

    # Пример 5: Обработка ошибок JSON
    handle_json_errors()

    # Пример 6: Сериализация пользовательского объекта
    serialize_custom_object()


if __name__ == "__main__":
    main()