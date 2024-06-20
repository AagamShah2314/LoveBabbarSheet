# 0. First and Last Position of an Element In Sorted Array


def firstAndLastPosition(arr, n, k):

    # Write your code here
    st=0
    en=n-1
    st1=-1
    en1=-1
    while st <= en:
        cen=(st+en)//2
        if arr[cen]==k:
            st1 = cen
            en1 = cen
            while st1 > 0 and arr[st1 - 1] == k:
                st1 -= 1
            # Find the last position
            while en1 < n - 1 and arr[en1 + 1] == k:
                en1 += 1
            return (st1, en1)
        elif arr[cen]>k:
            en=cen-1
        else:
            st=cen+1
    return (-1,-1)
pass
