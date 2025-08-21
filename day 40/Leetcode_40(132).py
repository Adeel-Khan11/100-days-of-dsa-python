class Solution(object):
    def longestConsecutive(self, nums):

        hm = {num: i for i, num in enumerate(nums)}
        for key in hm.keys():
          if (key - 1) not in hm:   
            hm[key] = True
        max_len=0
        for key in hm.keys():
            k=0
            if hm[key]==True:
             while (key+k) in hm:
                k+=1
            max_len=max(max_len,k)
        return max_len
            
       
obj=Solution()
# nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
nums=[]
# nums=[1,0,1,2]
print(obj.longestConsecutive(nums))
        