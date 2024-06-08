# 2.Kth Smallest and Largest Element of Array 
def kthSmallLarge(arr, n, k):
    # Write your code here
    arr.sort()
    return arr[k-1],arr[n-k]
    pass
