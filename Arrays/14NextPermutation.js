# 14. Next Permutation

from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(permutation, n):
    # Write your code here.
    i=n-2
    while (i>=0) and (permutation[i]>=permutation[i+1]):
        i=i-1;
    if(i>=0):
        j=n-1
        while (j>i) and (permutation[j]<=permutation[i]):
            j=j-1;
        permutation[j],permutation[i]=permutation[i],permutation[j]
    permutation[i + 1:] = reversed(permutation[i + 1:])
    return permutation if i >= 0 else sorted(permutation)
        
    # Return a list.
    pass
