# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 23:52:49 2017

@author: Administrator
"""

strs = input()
strs = strs.split(' ')
nums = [int(x) for x in strs]
N = nums[0]
Nums = nums[1:]
L1 = [x for x in Nums if x%5==0 and x%2==0]
L2 = [x for x in Nums if x%5==1]
L3 = [x for x in Nums if x%5==2]
L4 = [x for x in Nums if x%5==3]
L5 = [x for x in Nums if x%5==4]
A1 = sum(L1) if len(L1)!=0 else 'N'
if len(L2)==0:
    A2 = 'N'
else:
    A2 = 0
    cnt = 1
    for x in L2:
        A2 = A2 + x * cnt
        cnt = -cnt
A3 = len(L3) if len(L3)!=0 else 'N'
A4 = sum(L4)/len(L4) if len(L4)!=0 else 'N'
A5 = max(L5) if len(L5)!=0 else 'N'
ASum = [A1,A2,A3,A4,A5]
for item in ASum[0:-1]:
    if isinstance(item,float):
        print('%.1f' %item,end=' ')
    else:
        print(item, end=' ')
print(A5)
#strFinal = ' '.join(ASum)
#print(strFinal)

