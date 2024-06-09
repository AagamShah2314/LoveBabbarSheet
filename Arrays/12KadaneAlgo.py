#12. Kadane's Algorithm

def maxSubArraySum(self, arr, n):
        ##Your code here
        g_max=arr[0]
        l_max=arr[0]
        for num in arr[1:]:
            l_max = max(num, l_max + num)
            if g_max<l_max:
                g_max=l_max
        return g_max
