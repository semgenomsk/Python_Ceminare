"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt
(в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>
"""

from random inport randint

num = int(input("Введите число: "))
my_list = [randint(-num, num)] for _in range(num)]
print(my_list)

res = 1
with open('indexes.txt', 'r') as file:
    for line in file:
        index = int(line)
        if num > index >= num:
print(res)
