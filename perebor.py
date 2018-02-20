#!/usr/bin/env python3
# Метод последовательного перебора для вычисления наибольшего общего делителя для двух натуральных чисел

import random

m = random.randint(1,100)
n = random.randint(1,100)
print("m: ",m)
print("\nn: ",n)

t = min(m,n)
while t!=0:
    if m%t != 0:
        t = t-1
    else:
        if n%t !=0:
            t = t-1
        else:
            break
print("НОД: ", t)



