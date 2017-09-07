# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 09:14:23 2017

@author: Administrator
"""

strs = input()
strs = strs.split(' ')
n = int(strs[0])
m = int(strs[1])
P = int(strs[2])
L = list(range(0,n))
for x in range(0,n):
    strs = input()
    strs = strs.split(' ')
    L[x] = [int(ii) for ii in strs]
