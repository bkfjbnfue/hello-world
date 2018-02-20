#!/usr/bin/env python3

import sys
import random

def fac(n):
    fac = 1 
    i = 0 
    while i < n:
        i = i + 1
        fac = fac * i
    return fac

n = random.randint(0,10)
print(fac(n))
