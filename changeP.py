# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 09:39:15 2017

@author: Administrator
"""

# 进制转换
strs = input()
strs = strs.split(' ')
M = int(strs[0])
N = int(strs[1])
if M<0:
    negFlag = 1
    m = -M
else:
    negFlag = 0
    m = M
n = N


def num2str(it):
    num = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if it >= 10:
        strl = num[it]
    else:
        strl = str(it)
    return strl


chgRes = [];
while int(m / n) != 0:
    x = m % n;
    m = int(m / n)
    strl = num2str(x)
    chgRes.insert(0,strl)
strl = num2str(m)
chgRes.insert(0,strl)
if negFlag:
    chgRes.insert(0,'-')
strFin = ''.join(chgRes)
print(strFin)