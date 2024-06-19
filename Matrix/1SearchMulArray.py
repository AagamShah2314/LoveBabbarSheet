# 1.Search In A Row Wise And Column Wise Sorted Matrix

from os import *
from sys import *
from collections import *
from math import *

def search(matrix, x):
    # Write your code here.
    i = 0
    j = len(matrix[0])-1
    while j >= 0 and i < len(matrix[0]):
        if matrix[i][j] == x:
            return (i,j);
        elif matrix[i][j] > x:
            j = j - 1
        else:
            i = i + 1
    return (-1,-1);
    pass
