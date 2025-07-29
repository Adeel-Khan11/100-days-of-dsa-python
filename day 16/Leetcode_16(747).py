class Solution(object):
    def dominantIndex(self, nums):
        max_num1 = -1          
        max_num2 = -1          
        index_max = -1         
        
        for i, num in enumerate(nums):
            if num > max_num1:
                max_num2 = max_num1   
                max_num1 = num      
                index_max = i        
            elif num > max_num2:
                max_num2 = num      
        
        if max_num1 >= 2 * max_num2:
            return index_max
        else:
            return -1

obj=Solution()
nums=[3,6,1,0]
print(obj.dominantIndex(nums))  
       
    #    count=nums.count(max_num)
     
    
       
    