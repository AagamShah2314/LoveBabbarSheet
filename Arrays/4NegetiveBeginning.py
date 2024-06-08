# 3.Move All Negative Numbers To Beginning And Positive To End

from os import *
from sys import *
from collections import *
from math import *

def separateNegativeAndPositive(nums):
    # write your code here
    n=0;
    for i in range(len(nums)):
        if(nums[i]<0):
            nums[n],nums[i]=nums[i],nums[n]
            n+=1
    return nums
    pass
