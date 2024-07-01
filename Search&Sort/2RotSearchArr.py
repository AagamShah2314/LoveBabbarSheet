# 2.Search In Rotated Sorted Array

def search(arr, n, k):
    # Intialize the low,high
    low,high=0,n-1
    # Creating a binary search but modified as array is rotated
    while(low<=high):
        mid=(low+high)//2
        # If target(k) is present at mid 
        if arr[mid]==k:
            return mid
        # Now we know as array is rotated check which part is soretd
        # First checking if left part is sorted
        elif arr[low]<=arr[mid]:
            # If left part is sorted check if where element should lie
            # on the left or right portion
            if k<=arr[mid] and arr[low]<=k:
                high=mid-1
            else:
                low=mid+1
        # If the right is sorted
        else:
            # If right part is sorted check if where element should lie
            # on the left or right portion
            if k>=arr[mid] and arr[high]>=k:
                low=mid+1
            else:
                high=mid-1
    return -1
