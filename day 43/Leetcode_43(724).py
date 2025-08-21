class Solution(object):
    def pivotIndex(self, nums):
        right_sum=sum(nums)
        left_sum=0
          
        for i in range(0,len(nums)):
            right_sum-=nums[i]
            
            if(right_sum==left_sum):
                return i
            else:
                left_sum+=nums[i]
        return -1
       
obj=Solution()
# nums = [1,7,3,6,5,6]
# nums = [1,2,3]
# nums = [2,1,-1]
# nums=[]
print(obj.pivotIndex(nums))

    