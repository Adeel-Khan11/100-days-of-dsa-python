class Solution(object):
    def singleNonDuplicate(self, nums):
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if mid%2==1:
                mid-=1
            if nums[mid]==nums[mid+1]:
                left+=2
            else:
                right=mid
        return nums[left]
            
            
obj=Solution()
nums=[1,1,2,3,3,4,4,8,8]
# nums=[3,3,7,7,10,11,11]
# nums=[3,7,7,10,11,11]

print(obj.singleNonDuplicate(nums))
                
        
        