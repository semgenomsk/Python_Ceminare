from logger import log
import var
from tabulate import tabulate  # для установки библиотеки pip install tabulate


@log
def greeting():
    """ Приветствие """
    print('\n**Справочник студентов ВУЗА**')


@log
def menu():
    """ Меню """
    print("\nМеню:\n")
    print("0 - Выход\n"
          "1 - Добавить новую запись\n"
          "3 - Редактировать запись по id\n"
          "4 - Удаление записи\n")


@log
def print_data(data: list):
    """ Вывод в консоль данных содержимого справочника """
    print(tabulate(data, headers=var.field, tablefat="grid"))


def print_error():
    """ Сообщение об ошибки """
    print("Данные по id отсутствуют!")
