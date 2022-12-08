"""
Задать натуральное число k.
Сформируйте многочлен (полином) степени k со случайными коэффициентами из промежутка от 0 до 100, включительно.
Многочлен вывести в консоль и записать в файл.

Ввод: значение типа <int>
Вывод: значение типа <str>, файл с одной строкой.

Пример:
2
2x^2 + 4x + 5 = 0
"""

from random import randint


def create_poly(rotions):
    if sum(rotions) == 0:
        return ' = 0'

    power = len(rotions) + 1
    result = []
    for ratio in rotions:
        if ratio:
            if power == 0:
                result.append(f'{ratio}')
            elif power == 1:
                result.append(f'{ratio if ratio !=1 else ""}x')
            else:
                result.append(f'{ratio if ratio !=1 else ""}x^{power}')
        power += 1

    return ' + '.join(result) + ' = 0'


if __name__ == '__main__':
    k = int(input("Введите степень полиома k: "))
    rations = [randint(0, 100) for ratio in range(k)]

    polynom = create_poly(rations)
    print(polynom)