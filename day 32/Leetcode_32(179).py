from functools import cmp_to_key

class Solution(object):
   def largestNumber(self,nums):
       str_nums=list(map(str,nums))
       def comapre(a,b):
           if a+b>b+a:
               return -1
           else:
               return 1
       str_nums.sort(key=cmp_to_key(comapre))
       result=''.join(str_nums)
       return '0' if result[0]=='0' else result
   
   

# Example usage
nums = [3, 30, 34, 5, 9]
solution = Solution()
print(solution.largestNumber(nums))  # Output: "9534330"
