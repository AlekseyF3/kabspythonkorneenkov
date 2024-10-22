numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
a = sum(filter(None,numbers))
b = len(numbers)
aver = a/b
numbers[4] = aver
print("Измененный список:", numbers)
