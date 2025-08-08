class Solution(object):
    def maximumCount(self, nums):
       def first_zero(nums1):
         start=0
         end=len(nums1)
         while start<end:
             mid=(start+end)//2
             if nums1[mid]<0:
                 start=mid+1
             else:
                 end=mid
         return start
       def second_zero(nums2):
           start=0
           end=len(nums2)
           while start<end:
               mid=(start+end)//2
               if nums2[mid]<=0:
                   start=mid+1
               else:
                   end=mid
           return start
       neg_max=first_zero(nums)
       pos_max=len(nums)-second_zero(nums)
       return max(neg_max,pos_max)

        

obj=Solution()
# nums = [-2,-1,-1,1,2,3]
# nums=[-3,-2,-1,0,0,1,2]
nums = [5,20,66,1314]

print(obj.maximumCount(nums))
 
 
 
 
        
           
    
        