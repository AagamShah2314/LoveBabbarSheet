# 1. Check If The String Is A Palindrome

from os import *
from sys import *
from collections import *
from math import *


def checkPalindrome(s):
    # Write your code here
    l, r = 0, len(s) - 1
    
    while l < r:
        # Skip non-alphanumeric characters from the left
        while l < r and not s[l].isalnum():
            l += 1
        # Skip non-alphanumeric characters from the right
        while l < r and not s[r].isalnum():
            r -= 1
        # Compare the characters in a case-insensitive manner
        if s[l].lower() != s[r].lower():
            return False
        # Move pointers towards the center
        l += 1
        r -= 1
    return True
pass
