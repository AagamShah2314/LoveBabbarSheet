# 24. Given an array of size n and a number k, find all elements that appear more than " n/k " times.

from os import *
from sys import *
from collections import *
from math import *

def countTheNumber(arr, n, k):
    # Write your code here.
    dict={}
    ls=[]
    t=n//k
    for i in range(n):
        if arr[i] not in dict:
            dict[arr[i]]=0
        dict[arr[i]]+=1
        if dict[arr[i]]==t:
            ls.append(arr[i])
    return ls
    pass
