"""
Напишите игру "Крестики-нолики".
"""

from random import randint


def print_board(array: [list]):
    print('|', end=' ')
    print(*range(len(array)), sep=' | ', end=' | \n')
    print('-' * 13)
    for i, line in enumerate(array):
        print('|', end=' ')
        print(*line, sep=' | ', end=f' | {i}\n')
        print('-' * 13)

def check(array):
    

if __name__ == '__main__':
    lst = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    # print(lst)
    print("Начинаем игру крестики-нолики")
    players = ['0', 'X']
    turn = randint(0,1)
    player = players[turn]
    print_board(lst)
    while True:
        print(f'Ходит {players}')
        row, col = [int(i) for i in input("Укажите строку и столбец через пробел: ").split()]
        lst[row][col] = player  
        print_board(lst)
        turn = not turn
        player = players[turn]
