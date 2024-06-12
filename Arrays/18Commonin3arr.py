# 18.Common Elements In Three Sorted Arrays

from os import *
from sys import *
from collections import *
from math import *

def findCommonElements(a,b,c):
    # Write your code here.
    arr = []
    seen = set()
    n, m, o = 0, 0, 0
    j = len(a) 
    k = len(b)
    l = len(c)
    while (n < j) and (m < k) and (o < l):
        if a[n]==b[m] and b[m]==c[o]:
            if a[n] not in seen:
                arr.append(a[n])
                seen.add(a[n])
            n += 1
            m += 1
            o += 1
        elif a[n] < b[m]:
            n += 1
        elif b[m] < c[o]:
            m += 1
        else:
            o += 1 
    # Return a list containing all common elements.
    return arr
    pass
