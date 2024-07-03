# 23. Find longest consecutive subsequence

from math import *
from collections import *
from sys import *
from os import *

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    ar=set(arr)
    l=0
    for num in ar:
        if num-1 not in ar:
            cur=num
            c=1
            while cur+1 in ar:
                c+=1
                cur+=1
            l=max(l, c)
    return l
    pass
