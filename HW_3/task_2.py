"""
Задайте список целых чисел. Верните список с произведениями его парных элементов.
Парой считаются первый и последний элемент, второй и предпоследний и т.д.
Если элементов нечетное количество – центральный элемент умножается сам на себя.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[2, 3, 4, 5, 6]
[12, 15, 16]

[2, 3, 5, 6]
[12, 15]
"""

# Решение 1
# import randomn
# n = int(input("Введите чилсо N = "))
# my_list=[random.randint(0,n) for i in range(n)]
# print(my_list)

# new_list = []
# for i in range(0,(n + 1) // 2):
#     new_list.append(my_list[i] * my_list[- i - 1])
# print(new_list)

# Решение 2
import random
import math
size_list = int(input("Введите размер списка: "))
list_nums = [random.randint(0, 9) for i in range(size_list)]
result_list = []

for i in range(math.ceil(size_list / 2)):
    result_list.append(list_nums[i] * list_nums[- i - 1])
print(f"Исходынй список: {list_nums}")
print(f"Итоговый список: {result_list}")
# print(math.ceil(2.00001))