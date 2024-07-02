# 5. Find The Repeating And Missing Number


def findRepeatingAndMissingNumbers(nums):
    # Write your Code here.
    ans=[]
    ans2=[]
    n=len(nums)
    #l=nums[0]
    ls = [0]*(n+1)
    for num in nums:
        #num=num-l
        ls[num]+=1
    for i in range (1,n+1):
        if ls[i]==0:
            ans.append(i)
        if ls[i]>1:
            ans2.append(i)
    return ans2+ans
