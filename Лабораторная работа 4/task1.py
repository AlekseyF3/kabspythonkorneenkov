# TODO решите задачу
import json
def task(file):
    with open('input.json', 'r') as file:
        data = json.load(file) # читаем данные из файла

    sum = 0.0

    for item in data:
        score = item.get("score", 0)  # получаем значение по ключу "score"
        weight = item.get("weight", 0)  # получаем значение по ключу "weight"
        sum += score * weight  # Вычисляем произведение и добавляем к общей сумме

    return round(sum, 3)

json_path = 'input.json'
result = task(input)
print(result)
