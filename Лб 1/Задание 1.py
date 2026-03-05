numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_numbers = sum(x for x in numbers if x is not None)  # сумма элементов, кроме None
len_numbers = len(numbers)  # количество элементов списка, включая None
numbers[4] = sum_numbers / len_numbers  # замена
print("Измененный список:", numbers)
