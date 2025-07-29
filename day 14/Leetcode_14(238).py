class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        right = [1] * n  
        pro = 1
        for i in range(n - 1, -1, -1): 
            pro *= nums[i]
            right[i] = pro
       
        res=[0]*n
        left=1
        for i in range(0,n-1,1):
            val=left*right[i+1]
            res[i]=val
            left=left*nums[i]
        res[n-1]=left
        return res
        





        