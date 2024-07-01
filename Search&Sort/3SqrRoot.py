# 3.

import math

def floorSqrt(n):
   # write your code logic here .
   # a=int(math.sqrt(n))
   # return a
   l = 0
   r = n
   mid = (l+r) // 2
   while l<=r:
      sq = mid**2
      if sq==n:
         return mid
      elif sq < n:
         l = mid + 1
         a = mid
      else:
         r = mid - 1
      mid = (l+r) // 2
   return a
   
n= int(input())
print(floorSqrt(n))
