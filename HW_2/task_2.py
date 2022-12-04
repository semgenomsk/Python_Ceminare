"""
Напишите программу, которая принимает на вход натуральное число N и выдает список 
факториалов по основаниям от 1 до N

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
4
[1, 2, 6, 24]
"""

num = int(input("Введите число n: "))
my_list = []
factorial = 1
for i in range(1, num+1):
    factorial *= i
    my_list.append(factorial)

print(my_list)
