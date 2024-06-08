# 6. Rotate array

def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    a = arr[:k]
    b = arr[k:]
    return b+a
    pass
