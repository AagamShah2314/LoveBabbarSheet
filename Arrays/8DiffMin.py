#8. Minimize The Difference

from sys import *
from collections import *
from math import *

from typing import *

def minimizeIt(A: List[int], K: int) ->int:
    # Write your code here.
    A.sort()
    n=len(A)
    diff=A[-1]-A[0]
    new_min = A[0] + K
    new_max = A[-1] - K
    res=diff
    for i in range(n - 1):
        h = max(new_max, A[i]+K)
        l = min(new_min, A[i+1]-K)
        if l<0:
            continue
        res = min(res, h-l)
    return res
    pass

