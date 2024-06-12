# 21.Factorial Of Large Number

from os import *
from sys import *
from collections import *
from math import *

def calculateFactorial(n):
    #    Write your code here.
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
    pass
