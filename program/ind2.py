#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В списке, состоящем из вещественных элементов, вычислить:
# 1. номер минимального по модулю элемента списка;
# 2. сумму модулей элементов списка, расположенных
# после первого отрицательного элемента.
# Сжать список, удалив из него все элементы,
# величина которых находится в интервале [а, b].
# Освободившиеся в конце списка элементы заполнить нулями.

if __name__ == '__main__':
    input_list = [4.5, -2.7, 3.1, 4.2, -5.0, 6.3, 7.4, -8.9, 9.0]

    m_index = 0
    m_value = input_list[0]

    for i, num in enumerate(input_list):
        abs_value = abs(num)
        if abs_value < m_value:
            m_index = i
            m_value = abs_value
    summ = 0
    negative_found = False

    for num in input_list:
        if negative_found:
            summ += abs(num)
        elif num < 0:
            negative_found = True

    a = -4.0
    b = 6.0
    ind = 0
    
    for num in input_list.copy():
        if a <= num <= b:
            input_list.pop(ind)
            input_list.append(0)
        else:
            ind += 1

    print(f"Номер минимального по модулю элемента: {m_index}")
    print(f"Сумма модулей элементов после первого отрицательного: {summ}")
    print(f"Сжатый список: {input_list}")
