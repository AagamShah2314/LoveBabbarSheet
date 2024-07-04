# 26. Check Subset

from os import *
from sys import *
from collections import *
from math import *

def checkSubset(arr1, arr2, n, m):
    #Write your code here. 
    cnt={}
    for num in arr1:
        cnt[num] = cnt.get(num, 0)+1
    for num in arr2:
        if num not in cnt or cnt[num]==0:
            return False
        cnt[num]-=1
    return True
    pass
