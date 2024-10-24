# TODO Напишите функцию find_common_participants

def find_common_participants(first, second, znak=","):
    first_set = set(first.split(znak))
    second_set = set(second.split(znak))

    first = "Иванов|Петров|Сидоров"
    second = "Петров|Сидоров|Смирнов"

    common_participants = first_set.intersection(second_set)
    return sorted(list(common_participants))

# TODO Провеьте работу функции с разделителем отличным от запятой

first = "Иванов|Петров|Сидоров"
second = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(first, second, znak="|")
print(common_participants)