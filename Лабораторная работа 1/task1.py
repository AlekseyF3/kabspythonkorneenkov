numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_numbers = sum(filter(None, numbers))
length = len(numbers)
average = sum_numbers / length
numbers[4] = average
print("Измененный список:", numbers)
