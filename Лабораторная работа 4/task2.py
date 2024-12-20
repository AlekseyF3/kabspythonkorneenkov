import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        list = [row for row in csv_reader]

    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json.dump(list, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
