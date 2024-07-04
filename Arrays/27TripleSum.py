# 27. Find the triplet that sum to a given value

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit

def findTriplets(arr, n, k):
    arr=sorted(arr)
    res=[]
    for i in range(0, n-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        l=i+1
        r=n-1
        if arr[i] + 2 * arr[l] > k:
            break
        while l < r:
            sums=arr[l]+arr[i]+arr[r]
            if sums==k:
                t = [arr[i],arr[l],arr[r]]
                res.append(t)
                l+=1
                r-=1
                while l < r and arr[l] == arr[l-1]:
                    l += 1
                while l < r and arr[r] == arr[r+1]:
                    r -= 1
            elif sums<k:
                l+=1
            else:
                r-=1
    return res
    # Write your code here.
    pass

















# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    K = int(stdin.readline())
    return N, arr,K


tc = int(input())
while tc > 0:
    N, arr,K = takeInput()
    ans = findTriplets(arr, N,K)

    if len(ans) == 0:
        stdout.write("-1\n")

    else:
        for i in ans:
            i.sort()
            stdout.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

    tc -= 1
