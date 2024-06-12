# 19. Rearrange Alternatively

from os import *
from sys import *
from collections import *
from math import *

def rearrange(arr):
    neg = 0
    for i in range(0, len(arr)-1):
        if arr[i] < 0:
            arr[neg], arr[i] = arr[i], arr[neg]
    return arr
    # Write your code here.
