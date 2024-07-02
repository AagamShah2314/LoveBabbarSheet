# 7. Majority element

from math import *
from collections import *
from sys import *
from os import *

def findMajorityElement(arr, n):
	# Dictionary to store the frequency of each element
    # freq = {}
    # majority_element = None
    # max_count = 0

    # # Count the frequency of each element in the array
    # for i in range(n):
    #     if arr[i] in freq:
    #         freq[arr[i]] += 1
    #     else:
    #         freq[arr[i]] = 1

    #     # Update the majority element if the current element's count is greater
    #     if freq[arr[i]] > max_count:
    #         majority_element = arr[i]
    #         max_count = freq[arr[i]]

    # # Check if the majority element occurs more than n // 2 times
    # if max_count > n // 2:
    #     return majority_element
    # else:
    #     return -1
	# Phase 1: Find a candidate for the majority element
    candidate = None
    count = 0
    
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    # Phase 2: Verify if the candidate is actually the majority element
    count = sum(1 for num in arr if num == candidate)
    
    if count > n // 2:
        return candidate
    else:
        return -1
