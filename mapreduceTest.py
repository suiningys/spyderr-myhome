# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:49:44 2017

@author: Administrator
"""
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
#    strList = list(name)
#    strList[0] = strList[0].upper()
#    strList2 = strList[1:]
#    strList2 = [s.lower() for s in strList2]
#    strList = strList[0:1] + strList2
#    strRes = ''.join(strList)
    strRes = name.capitalize()
    return strRes
print(normalize('sOL'))
r = map(normalize,['adam', 'LISA', 'barT'])
#编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce

def mutp(x1,x2):
    return x1 * x2

def prod(L):
    res = reduce(mutp,L)
    return res
    
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def not_empty(s):
    return s and s.strip()

#filter
def is_palindrome(n):
    str1 = list(str(n))
    for x in range(0,len(str1)):
        if str1[x]!=str1[-1-x]:
            return False
    return True
output = filter(is_palindrome, range(1, 1000))
print(list(output))