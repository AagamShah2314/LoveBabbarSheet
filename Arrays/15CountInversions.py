# 15. Count Inversions

from os import *
from sys import *
from collections import *
from math import *

def merge(arr, l, mid, r):
    inv = 0
    n1 = mid - l + 1
    n2 = r - mid
    left = [0] * n1
    right = [0] * n2
    
    for i in range(n1):
        left[i] = arr[l + i]
        
    for j in range(n2):
        right[j] = arr[mid + 1 + j]
    
    i, j, k = 0, 0, l
    
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            inv += n1 - i  # Count inversions
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
    
    return inv

def mergeSort(arr, l, r):
    inv = 0
    if l < r:
        mid = (l + r) // 2
        inv += mergeSort(arr, l, mid)
        inv += mergeSort(arr, mid + 1, r)
        inv += merge(arr, l, mid, r)
    return inv

def getInversions(arr, n):
    return mergeSort(arr, 0, n - 1)

# Taking input using fast I/O.
def takeInput():
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))
