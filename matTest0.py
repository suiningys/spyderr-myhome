# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 15:31:37 2017

@author: Administrator
"""


#import math
#import numpy
from numpy import *
vector1 = mat([1,2,3])
vector2 = mat([4,5,6])
print(sqrt((vector1-vector2)*(vector1-vector2).T))

print(dot(vector1,vector2.T)/(linalg.norm(vector1)*linalg.norm(vector2)))

import numpy as np

# 2-D array: 2 x 3
two_dim_matrix_one = np.array([[1, 2, 3], [4, 5, 6]])
# 2-D array: 3 x 2
two_dim_matrix_two = np.array([[1, 2], [3, 4], [5, 6]])

two_multi_res = np.dot(two_dim_matrix_one, two_dim_matrix_two)
print('two_multi_res: %s' %(two_multi_res))

from numpy import *
import scipy.spatial.distance as dist
matV = mat([[1,1,1,1],[1,0,0,1]])
print(dist.pdist(matV,'jaccard'))