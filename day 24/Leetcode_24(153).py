class Solution(object):
    def findMin(self, nums):
        left=0
        right=len(nums)-1
         
        while left<=right:
            mid=(left+right)//2
            if left==right:
                return nums[left]      
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
            
            
obj=Solution()
# [4,5,6,7,0,1,2]
nums=[11,13,15,17]
print(obj.findMin(nums)) #
            
        
        