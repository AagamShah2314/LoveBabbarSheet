# 3. Duplicate Characters

from sys import *
from collections import *
from math import *

from typing import *

def duplicate_char(s: str, n: int) -> List[Tuple[chr, int]]:
    # Write your code here.
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    duplicates = [(char,count) for char, count in char_count.items() if count > 1]
    duplicates.sort()
    return duplicates
    pass
