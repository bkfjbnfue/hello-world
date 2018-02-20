#!/usr/bin/env python3

import sys

def fac(n):
    if n==0:
        return 1
    return fac (n-1) * n

n = int(sys.argv[1])
print(fac(n))
