#!/usr/bin/env python3

import random

def first_function(a,b,c):
    if a>b:
        return b+c
    else:
        return a+c

a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
print("a: ", a, "\nb: ", b, "\nc: ", c, "\nresult: ", first_function(a,b,c))
