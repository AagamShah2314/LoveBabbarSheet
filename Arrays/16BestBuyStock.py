# 16.Best Time to Buy and Sell Stock

from os import *
from sys import *
from collections import *
from math import *
def maximumProfit(prices):
    # Write your code here.
    if not prices:
        return 0
    l = prices[0]
    diff = 0
    for i in range(1, len(prices)):
        if prices[i] < l:
            l = prices[i]
        else:
            diff = max(diff, prices[i] - l)
    return diff
