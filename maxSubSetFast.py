# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 15:38:34 2017

@author: Administrator
"""

numberStr = input()
numberStrs = numberStr.split(' ');
numbers = [int(x) for x in numberStrs]
#numbers = sys.stdin.readline().split()
summary = numbers[0];
firstPost = -1;
lastPost = len(numbers)
for ii in range(0,len(numbers)):
    if numbers[ii]>0:
        firstPost = ii
        break
for ii in range(len(numbers)-1,-1,-1):
    if numbers[ii]>0:
        lastPost = ii;
        break
if(firstPost==-1&lastPost==len(numbers)):
    summary = max(numbers)
elif firstPost==lastPost:
    summary = numbers[firstPost]
else:
    fixNumbers = numbers[firstPost:lastPost+1]
    for ii in range(0,len(fixNumbers)):
        for jj in range(ii,len(fixNumbers)):
            subSet = fixNumbers[ii:jj]
            summaryTemp = sum(subSet)
            if(summaryTemp>summary):
                summary = summaryTemp
print(summary)