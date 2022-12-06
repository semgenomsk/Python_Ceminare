"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""

import random
size = int(input("Введите целое число: "))
list_num = [round(random.uniform(0, 9), 2) for i in range(size)]
drob_num = []
for i in range(0, len(list_num)):
    n = int(list_num[i] * 100) % 100
    drob_num.append(n)
max_drob = max(drob_num)
min_drob = min(drob_num)
print(list_num)
print((max_drob - min_drob) / 100)
