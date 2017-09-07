# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 23:45:44 2017

@author: Administrator
"""

T = input()
T = int(T)
for ii in range(0,T):
    strs = input()
    strs = strs.split(' ')
    nums = [int(x) for x in strs]
    if nums[0]+nums[1]>nums[2]:
        print('Case #%d: true' %(ii+1))
    else:
        print('Case #%d: false' %(ii+1))