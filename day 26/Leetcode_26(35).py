class Solution(object):
    def searchInsert(self, nums, target):
        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return left
    
obj=Solution()
# target=5
# target=2
target=7  
nums = [1,3,5,6]
print(obj.searchInsert(nums,target))  
