def find_common_participants(first, second, sign=","):
    first_set = set(first.split(sign))
    second_set = set(second.split(sign))

    common_participants = first_set.intersection(second_set)
    return sorted(list(common_participants))


first = "Иванов|Петров|Сидоров"
second = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(first, second, sign="|")
print(common_participants)
