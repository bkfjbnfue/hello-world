#!/usr/bin/env python3
# Алгоритм Евклида для вычисления наибольшего общего делителя для двух натуральных чисел

import random

m = random.randint(0,1000)
n = random.randint(0,1000)
print("m: ",m)
print("\nn: ",n)

while n != 0:
    k = m%n
    m = n
    n = k

print("НОД: ", m)
