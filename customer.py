# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 23:22:52 2017

@author: Administrator
"""

strs = input()
strs = strs.split(' ')
n = int(strs[0])
m = int(strs[1])
strs = input()
strs = strs.split(' ')
vols = [int(x) for x in strs]
inf = [list(range(0,m)),list(range(0,m))]
for x in range(0,m):
    strs = input()
    strs = strs.split(' ')
    inf[0][x] = strs[0]
    inf[1][x] = strs[1]

