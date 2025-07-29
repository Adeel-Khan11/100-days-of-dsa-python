class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

obj=Solution()
nums=[1,2,3,4,5,63,4,3,3]
val=3
print(obj.removeElement(nums,val))
            
      
        