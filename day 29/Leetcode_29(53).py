class Solution(object):
    def maxSubArray(self, nums):
        current_sum=0
        max_sum=float('-inf')
        i=0
        end=len(nums)
        while i<end:
            current_sum+=nums[i]
            max_sum=max(current_sum,max_sum)
            if current_sum<0:
                current_sum=0
            i+=1
        return max_sum
obj=Solution()
# nums=[-2,1,-3,4,-1,2,1,-5,4]
# nums=[1]
nums=[5,4,-1,7,8]
print(obj.maxSubArray(nums))
        
        