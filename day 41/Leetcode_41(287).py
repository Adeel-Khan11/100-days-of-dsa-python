

class Solution(object):
    def findDuplicate(self, nums):
        ans=0
        
        for i in range(0,len(nums)):
            element=nums[i]
            element=abs(element)
            
            if nums[element]>0:
                nums[element]=-nums[element]
            else:
                ans=element
                break
        for i in range(0,len(nums)):
            nums[i]=abs(nums[i])
            
        return ans
    
    
    
obj=Solution()

# nums = [3,1,3,4,2]
# nums=[1,3,4,2,2]
nums=[3,3,3,3,3]
print(obj.findDuplicate(nums))
        