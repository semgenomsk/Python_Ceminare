"""
Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
[2, 4, 6, 8]
"""

user_set = [int(i) for i in input('Введите последовательность чисел: ').split()]
sl = {}
res_list = []

for el in user_set:
    sl[f'{el}'] = user_set.count(el)

for key, value in sl.items():
    if value == 1:
        res_list.append(int(key))

print(res_list)