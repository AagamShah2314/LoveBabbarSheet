# 0.Spiral Matrix

from os import *
from sys import *
from collections import *
from math import *

import sys
from sys import stdin

def spiralPathMatrix(matrix, n, m):
    # Write your code here.
    top, bottom, left, right = 0, n-1, 0, m-1
    arr = []
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            arr.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            arr.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                arr.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                arr.append(matrix[i][left])
            left += 1
    return arr
    pass





t = int(input().strip())

for j in range(t):
    
    n, m = list(map(int, stdin.readline().strip().split(" ")))
    
    arr = []
    
    for i in range(n):
        
        a = list(map(int, stdin.readline().strip().split(" ")))
        arr.append(a)
            
    
    for i in spiralPathMatrix(arr, n, m):
        print(i, end = " ")
        
    print()
