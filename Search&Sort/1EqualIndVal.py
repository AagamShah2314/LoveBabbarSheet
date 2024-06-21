# 1. Value Equal To The Index Value

from os import *
from sys import *
from collections import *
from math import *

def valueEqualToIndices(numArray, n):
    # Write your code here.
    ls=[]
    for i in range(0,n):
        if i == numArray[i]:
            ls.append(i)
        i += 1
    return ls if len(ls) > 0 else [-1]
    pass
