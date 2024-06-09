# 10.Duplicate In Array

def findDuplicate(arr):
    # Write your code here
    arr.sort()
    for i in range(0,len(arr)-1):
        if arr[i]==arr[i+1]:
            return arr[i]
    pass
