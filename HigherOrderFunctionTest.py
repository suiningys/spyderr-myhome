# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 23:39:56 2017

@author: Administrator
"""

def add(x,y,f):
    return f(x)+f(y)

add(-1,-3,abs)

def power(x,n=2):
    res = 1
    for ii in range(0,n):
        res = res * x
    return res
r = map(power,list(range(1,10)))
L = list(r)
from functools import reduce
def add(x,y):
    return x+y
reduce(add,list(range(1,10,2)))

