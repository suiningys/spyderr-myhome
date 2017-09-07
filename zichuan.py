# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 15:29:30 2017

@author: Administrator
"""

#zichuan
strs = input()
strs = strs.split(' ')
numbers = [int(x) for x in strs]
k = int(input())
numbers = sorted(numbers)
kMax = numbers[-k]
print(kMax)