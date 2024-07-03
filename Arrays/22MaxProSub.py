# 22.find maximum product subarray

from os import *
from sys import *
from collections import *
from math import *

def maximumProduct(arr, n):
    # write your code here
    res=mini=maxi=arr[0]
    for num in arr[1:]:
        if num<0:
            mini, maxi=maxi, mini
        maxi = max(num, maxi*num)
        mini = min(num, mini*num)
        res = max(res, maxi)
    return res
    # Return an integer denoting the answer to the required problem 
    pass
