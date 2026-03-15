import json

# -----------------------------
# ДАННЫЕ ДЛЯ ПРИМЕРА
# -----------------------------
data = {
    "name": "Ivan",
    "age": 25,
    "skills": ["Python", "SQL", "API"]
}

file_name = "data.json"


# -----------------------------
# ЗАПИСЬ JSON В ФАЙЛ
# -----------------------------
def write_json():
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("JSON записан")


# -----------------------------
# ЧТЕНИЕ JSON ИЗ ФАЙЛА
# -----------------------------
def read_json():
    with open(file_name, "r", encoding="utf-8") as f:
        content = json.load(f)
    print("JSON прочитан:")
    print(content)
    return content


# -----------------------------
# ОБНОВЛЕНИЕ JSON
# -----------------------------
def update_json():
    content = read_json()
    content["age"] = 30
    content["city"] = "Moscow"

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(content, f, indent=4, ensure_ascii=False)

    print("JSON обновлён")


# -----------------------------
# JSON СТРОКА → PYTHON ОБЪЕКТ
# -----------------------------
def json_string_to_object():
    json_string = '{"name": "Anna", "age": 22}'
    obj = json.loads(json_string)
    print("Строка → объект:", obj)


# -----------------------------
# PYTHON ОБЪЕКТ → JSON СТРОКА
# -----------------------------
def object_to_json_string():
    obj = {"car": "BMW", "year": 2020}
    json_string = json.dumps(obj, indent=4)
    print("Объект → строка:")
    print(json_string)


# -----------------------------
# ЗАПУСК
# -----------------------------
if __name__ == "__main__":
    write_json()
    read_json()
    update_json()
    json_string_to_object()
    object_to_json_string()