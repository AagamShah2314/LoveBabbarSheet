# 17.Pair Sum

from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, n, target):
    # Write your code here.
    l = 0
    r = n - 1
    c = 0
    while(l<r):
        if (arr[r] + arr[l] - target) > 0:
            r = r - 1
        elif (arr[r] + arr[l] - target) < 0:
            l = l + 1
        else:
            c = c + 1
            l = l + 1
            r = r - 1
    if c == 0:
        return -1
    return c 
    pass
