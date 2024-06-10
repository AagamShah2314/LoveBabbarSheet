# 13.Merge Intervals

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit

class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

def mergeIntervals(intervals):
    # Write your code here.
    merged = []
    intervals.sort(key=lambda x: x[0])
    for interval in intervals[l:]:
        if interval[0]<=prev[1]:
            prev[1]=max(interval[1],prev[1])
        else:
            merged.append(prev);
            prev=interval;
    merged.append(prev)
    return merged
    pass
    

n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)
