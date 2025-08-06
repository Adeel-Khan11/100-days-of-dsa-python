class Solution(object):
    def targetIndices(self, nums, target):
      result=[]
      num_count=0
      target_count=0
      for i in range(0,len(nums)):
          if nums[i]==target:
              target_count+=1
          elif nums[i]<target:
              num_count+=1
      while (target_count>0):
          result.append(num_count)
          target_count-=1
          num_count+=1
      return result
         
obj=Solution()
# nums=[1,2,5,2,3]
# target=2
# nums = [1,2,5,2,3]
# target = 3
nums = [1,2,5,2,3]
target = 5
print(obj.targetIndices(nums,target))  # Output
        
        
          
        