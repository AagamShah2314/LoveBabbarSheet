# 7.Maximum Subarray Sum

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

	# Your code here
    if n == 0:
        return 0
    g_max = arr[0]
    l_max = arr[0]
    for i in range(1, n):
        l_max = max(arr[i], arr[i] + l_max)
        if l_max > g_max:
            g_max = l_max
    # return the answer
    return max(g_max, 0)


#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
