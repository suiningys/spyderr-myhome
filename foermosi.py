# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 00:26:07 2017

@author: Administrator
"""

week = {1:'MON' ,2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT', 7:'SUN'}
exp = []
for x in range(0,24):
    if x <10:
        exp[x] = str(x)
    else:
        exp[x] = 'A'