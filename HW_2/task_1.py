"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Ввод: значение типа <float>
Вывод: значение типа <int>

Примеры:
6782.0
23

0.56
11
"""

num=float(input("Введите вещественное число: "))
sum=0
for i in str(num):
    if i!="."and i!= ",":
        sum+=int(i)
print(sum)