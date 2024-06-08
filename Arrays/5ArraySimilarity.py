#5.Find similarities between two arrays.

from os import *
from sys import *
from collections import *
from math import *

def findSimilarity(arr1, arr2, n, m):

    # Write your code here.
    arr3=arr1+arr2
    un=0
    si=0
    dict={}
    for i in range(len(arr3)):
        if arr3[i] in dict:
            dict[arr3[i]] += 1
        else:
            dict[arr3[i]] = 1
        if dict[arr3[i]] > 1:
            si += 1
    un=m+n-si
    return si,un
    pass
