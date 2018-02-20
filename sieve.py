#!/usr/bin/env python3

#Решето Эратосфена - алгоритм генерации последовательности простых чисел
# не превышающих произвольно заданного целого числа

import random
import math

def eratosthenes(n):     
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

n = random.randint(1,1000)
print("n: ",n)
L = list(filter(lambda x: x!=0, eratosthenes(n))) 
print(L)
