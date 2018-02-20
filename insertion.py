#!/usr/bin/env python3

import random

a = [random.randint(1,50) for _ in range(10)]
t = len(a)
for i in range (1, t):
    x=a[i]
    while (x < a[i-1] and i>0):
        a[i]=a[i-1]
        i=i-1
    a[i]=x
    print(a)
print("Итог: ",a)
