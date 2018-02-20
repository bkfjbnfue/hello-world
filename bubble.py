#!/usr/bin/env python3

import random

a = [random.randint(1,50) for _ in range(100)]
n = len(a)
for j in range (1, n):
    for i in range (1, n):
        if a[i]<a[i-1]:
            temp = a[i]
            a[i] = a[i-1]
            a[i-1] = temp

print("Итог: ", a)
