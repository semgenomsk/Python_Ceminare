"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""

str_text = "автомобиль букварь вариант пошел снег автобус"
str_num = []

value = str_text.split()
for i in value:
    if "а" not in i and "б" not in i and "в" not in i:
        str_num.append(i)
        
result = " ".join(str_num)
print(result)