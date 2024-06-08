/* 1.Sum Of Max And Min */

from os import *
from sys import *
from collections import *
from math import *

def sumOfMaxMin(arr):
    # Write your code here
    max=arr[0]
    min=arr[0]
    for i in range(0,len(arr)):
        if min>arr[i]:
            min=arr[i]
        if max<arr[i]:
            max=arr[i]
    return min+max
    pass

