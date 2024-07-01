# 4.Middle Of Three

from sys import *
from collections import *
from math import *

def middleOfThree(x:int, y:int, z:int):
    # Write your code here
    # ma = max(x,y,z)
    # mi = min(x,y,z)
    # return (x+y+z-mi-ma)
    arr=[x,y,z]
    arr.sort()
    return(arr[1])
    # Return an integer
    pass
