# 10. Duplicate In Array

def findDuplicate(arr):
    # Write your code here
    seen=set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    pass
