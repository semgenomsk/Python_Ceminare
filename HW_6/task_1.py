"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.

Ввод: значение типа <str>
Вывод: значение числового типа данных
"""

def find(exp, sech_operand):
    index_start = 0
    index_finished = 0
    index_operand = 0
    operands_full = ['*', '/', '-', '+']
    operands = ['*', '/', '-', '+']
    for op in sech_operand:
        operands.remove(op)
    found = False
    for i, sym in enumerate(exp):
        if i == 0 and sym == '-':
            continue
        if not found and sym in operands:
            index_start = i+1
        elif found and sym in operands_full:
            index_finished = i-1
            return index_start, index_finished, index_operand
        elif sym in sech_operand:
            found = True
            index_operand = index_finished = len(exp)-1
    return index_start, index_finished, index_operand

def calc(exp):
    if '*' in exp or '/' in exp:
        ind_s, ind_f, ind_o = find(exp, ['*', '/'])
        if exp[ind_o] == '*':
            exp = exp[0:ind_s] + str(float(exp[ind_s:ind_o])
                                     * float(exp[ind_o+1:ind_f+1])) + exp[ind_f+1:]
            exp = calc(exp)
        elif exp[ind_o] == '/':
            exp = exp[0:ind_s] + str(float(exp[ind_s:ind_o]) /
                                     float(exp[ind_o+1:ind_f+1])) + exp[ind_f+1:]
            exp = calc(exp)

    if '+' in exp or '-' in exp:
        ind_s, ind_f, ind_o = find(exp, ['+', '-'])
        if exp[ind_o] == '+':
            exp = exp[0:ind_s] + str(float(exp[ind_s:ind_o]) +
                                     float(exp[ind_o+1:ind_f+1])) + exp[ind_f+1:]
            exp = calc(exp)
        elif exp[ind_o] == '-':
            exp = exp[0:ind_s] + str(float(exp[ind_s:ind_o]) -
                                     float(exp[ind_o+1:ind_f+1])) + exp[ind_f+1:]
            exp = calc(exp)
    return exp

if __name__ == '__main__':
    exp = "3 / 4 * 2"
    print(calc(exp))