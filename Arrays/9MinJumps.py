# 9.Minimum Jumps

def minimumJumps(arr, n):

    # write your code here
    
    # If the array has only one element, no jump is needed
    if n <= 1:
        return 0
    # If the first element is 0, it is not possible to jump anywhere
    if arr[0] == 0:
        return -1
    c_i=arr[0]
    f_i=arr[0]
    s=1
    for i in range(0,n-1):
        f_i=max(f_i, i+arr[i])
        if i==c_i:
            c_i=f_i
            s+=1    
        if c_i<=i:
            return -1
    return s
    pass
