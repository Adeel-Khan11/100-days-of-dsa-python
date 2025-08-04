class Solution(object):
    def findPeakElement(self, nums):
        
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if left==right:
                return left
            if nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                right=mid
obj=Solution()
# nums=[1,2,1,3,5,6,4]
nums=[1,2,3,1]
print(obj.findPeakElement(nums))
        
        