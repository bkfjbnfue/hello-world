#!/usr/bin/env python3

import random

array = [random.randint(1,10) for _ in range(10)]
print('Исходный: ', array)


def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        print(q)
        L = [elem for elem in A if elem < q]
        print('L: ', L)
        M = [q] * A.count(q)
        print('[q]: ', [q])
        print('A.count(q): ', A.count(q))
        R = [elem for elem in A if elem > q]
        print('R: ', R)
        return QuickSort(L) + M + QuickSort(R)

x = QuickSort(array)
print("Итог: ",x)
