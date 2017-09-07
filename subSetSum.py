# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 22:29:48 2017

@author: Administrator
"""

#import sys
n = input()
numberStr = input()
numberStrs = numberStr.split(' ');
numbers = [int(x) for x in numberStrs]
#numbers = sys.stdin.readline().split()
summary = 0;
for ii in range(0,len(numbers)):
    for jj in range(ii,len(numbers)):
        subSet = numbers[ii:jj]
        summaryTemp = sum(subSet)
        if(summaryTemp>summary):
            summary = summaryTemp
print(summary)