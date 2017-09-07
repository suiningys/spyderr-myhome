# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 23:26:13 2017

@author: Administrator
"""

import json
path = r'F:\MyProjects\pydata-book\ch02\usagov_bitly_data2012-03-16-1331923249.txt'
record = [json.loads(line) for line in open(path)]
timeZones = [rec['tz'] for rec in record if 'tz' in rec]

from collections import defaultdict

def getCount(seq):
    counts = defaultdict(int)
    for x in seq:
        counts[x] +=1
    return counts
counts = getCount(timeZones)

def topCounts(couts,n = 10):
    valueKeyPairs = [(count,tz) for tz,count in counts.items()]
    valueKeyPairs.sort()
    return valueKeyPairs[-n:]

print(topCounts(counts))

from collections import Counter
counts = Counter(timeZones)
counts.most_common(10)

from pandas import DataFrame,Series
import pandas as pd;
import numpy as np
frame = DataFrame(record)
tzCounts = frame['tz'].value_counts()