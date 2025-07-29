from collections import Counter
class Solution(object):
    def findLucky(self, arr):
        frequency=Counter(arr)
        max2=-1
        for num,count  in frequency.items():
           if num==count:
             max2=max(max2,num)
        return max2
obj=Solution()
arr=[2,2,2,3,3]
print(obj.findLucky(arr))
            
       
        