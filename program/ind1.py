#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, 
# найти произведение положительных элементов кратных 3,
# их количество и вывести результаты на экран.

if __name__ == '__main__':
    print("Введите список элементов (через пробел):")
    A = list(map(int, input().split()))

    product = 1
    count = 0
    B = list(filter(lambda x:x > 0 and x % 3 == 0, A))
    count = len(B)
    for num in B:
        product *= num

    print(f"Произведение положительных элементов, кратных 3: {product}")
    print(f"Количество положительных элементов, кратных 3: {count}")
