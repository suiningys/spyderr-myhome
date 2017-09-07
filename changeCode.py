# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:59:45 2017

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

def calSon(m,n):
    if(m>n):
        big = m
        small = n
    else:
        big = n
        small = m
    while(big):
        small, big = big, small%big
    return small
        
strTemp = input()
target = list()
while(strTemp!=''):
    target.append(int(strTemp))
    strTemp = input()
for ii in range(0,len(target)):
    tarTemp = target[ii]
    codeAll = list()
    for jj in range(2,tarTemp):
        codeAll.extend(changCode(tarTemp,jj))
    sumTemp = sum(codeAll)
    mother = tarTemp-2
    son = calSon(sumTemp,mother)
    sumTemp = sumTemp/son
    mother = mother/son
    print('%d/%d' %(sumTemp,mother))