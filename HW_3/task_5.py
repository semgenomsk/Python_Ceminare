"""
Задайте целое число N.
Составьте список чисел Фибоначчи размерность 2N + 1 для отрицательной 
и положительной части (Негафибоначчи).
https://ru.wikipedia.org/wiki/Негафибоначчи

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
8
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

# Решение 1
from datetime import datetime

number = int(input("Введите натуральное число: "))
start = datetime.now()
my_list = [0 for _ in range(number * 2 + 1)]
my_list[number + 1] = my_list[number - 1] = 1
for i in range(number - 1):
    my_list[number + 2 + i] = my_list[number + 1 + i] + my_list[number + i]
    my_list[number - 2 - i] = my_list[number + 2 + i] * ((-1) ** (i+1))
print(datetime.now() - start)
print(my_list)

# Решение 2 - некорректно работает
num = int(input('Введите целое число: '))
# start=datetime.now()
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

list_fib = []
for i in range(1, num + 1):
    list_fib.append(fib(i))

print(list_fib)

def neg_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return neg_fib(n - 1) + 1
    else:
        return neg_fib(n - 2) + 1 + neg_fib(n - 1)

list_neg_fib = []
for i in range(num, -1, -1):
    list_neg_fib.append(neg_fib(i))
print(list_neg_fib + list_fib)
# print(datetime.now() - start)
