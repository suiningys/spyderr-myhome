# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 22:31:22 2017

@author: Administrator
"""

import numpy as np
import pandas
import matplotlib.pyplot as plt
x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)

L = [x*x for x in range(0,10)]
L = [x*x for x in range(0,10) if x%2==0]
Strs = [m + n for m in 'XYA' for n in 'ABC']

import os
[d for d in os.listdir('.')]
strs = 'abc'
isinstance(strs,str)
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]

from collections import Iterator
isinstance((x for x in range(0,10)),Iterator)