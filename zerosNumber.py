# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 09:30:00 2017

@author: Administrator
"""

str = input()
n = int(str)
fiveNum = 0;
for x in range(1,n+1):
    if x%125==0:
        fiveNum+=3
    elif x%25==0:
        fiveNum+=2
    elif x%5==0:
        fiveNum+=1
print(fiveNum)
        