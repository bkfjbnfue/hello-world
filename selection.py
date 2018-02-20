#!/usr/bin/env python3

import random

a = [random.randint(1,50) for _ in range(10)]
t = len(a)
print(a)
for i in range (0,t):
    minimum=a[i]
    for j in range (i,t):
        if a[j]<minimum:
            minimum = a[j]
            a[j] = a[i]
        a[i]=minimum
    print(a)
print("Итог: ",a)
