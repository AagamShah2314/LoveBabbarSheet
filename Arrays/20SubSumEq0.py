# 20.Find if there is any subarray with sum equal to 0

from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):

    # Write your code here
    c = 0
    seen = set()
    for i in  range(0, n-1):
        if k - arr[i] not in seen:
            seen.add(k - arr[i])
    for i in range (0, n-1):
        if arr[i] in seen:
            return True
    if 0 in seen:
        return True
    return False
    # Return a boolean variable 'True' or 'False' denoting the answer
    pass
    
    
    

