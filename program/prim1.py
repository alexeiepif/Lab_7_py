#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


if __name__ == '__main__':
    # Ввести список одной строкой.
    A = list(map(int, input().split()))
    # Проверить количество элементов списка.
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    # Найти искомую сумму 1.
    s = 0
    for item in A:
        if abs(item) < 5:
            s += item
    print(s)
    s = 0
    # Найти искомую сумму 2.
    s = sum([a for a in A if abs(a) < 5])
    print(s)