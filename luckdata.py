# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 22:45:03 2017

@author: Administrator
"""

def changCode(m,n):
    res = list();
    mTemp = m
    nTemp = n
    while(mTemp!=0):
        res.insert(0,mTemp%nTemp)
        mTemp = int(mTemp/nTemp)
    return res

n = int(input())
luckNum = 0
for ii in range(1,n+1):
    if(sum(changCode(ii,2))==sum(changCode(ii,10))):
        luckNum = luckNum+1
print(luckNum)