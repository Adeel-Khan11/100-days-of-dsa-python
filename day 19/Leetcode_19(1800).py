class Solution(object):
    def maxAscendingSum(self, nums):
        curr_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            
          
            if curr_sum > max_sum:
                max_sum = curr_sum
        
        return max_sum

                
obj=Solution()
nums=nums = [10, 20, 30, 5, 10, 1]

print(obj.maxAscendingSum( nums))
                
        