"""
Задайте список целых чисел. Найдите сумму элементов списка, имеющих нечетные индексы.

Ввод: значение типа <list> (либо значение типа <int> – размерность списка)
Вывод: значение типа <int>

Примеры:
[2, 3, 5, 9, 3]
12

[5, 1, 5, 2, 7, 11]
14
"""

import random
size_list = int(input("Введите размер списка: "))
list_num = [random.randint(0, 9) for i in range(size_list)]

sum = 0
for i in range(1, len(list_num), 2):
    sum += list_num[i]
print(f"Исходный список: {list_num}")
print(f"Сумма элементов списка, имеющих нечетные индексы, составляет: {sum}")