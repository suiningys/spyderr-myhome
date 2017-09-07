# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 10:19:03 2017

@author: Administrator
"""

#数字和为sum
strs = input()
strs = strs.split(' ')
n = int(strs[0])
tarSum = int(strs[1])
strs = input()
strs = strs.split(' ')
A = [int(x) for x in strs]

from numpy import *
import matplotlib.pyplot as plot
import pandas
plot(range(5))