# 4. Check If One String Is A Rotation Of Another String

def isCyclicRotation(p: str, q: str) -> int:
    # Write your code here.
    if len(p)!=len(q):
        return 0
    p = p + p
    if q in p:
        return 1
    else:
        return 0
    pass
