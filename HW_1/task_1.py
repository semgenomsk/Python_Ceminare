"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.

Ввод: значение типа <int>
Вывод: единственное значение типа <bool> (True либо False)

Пример:
6
True

7
True

1
False
"""

num = int(input("Введите день недели от 1 до 7: "))

if num < 1 or num > 7:
    print("Номер недели введен некорректно!")
elif num == 6 or num == 7:
    print("Выходной! Ура!")
else:
    print("Вставать пора, собирайтесь на работу!")
