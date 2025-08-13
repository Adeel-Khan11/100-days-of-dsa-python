class Solution(object):
    def plusOne(self, digits):
        digits=int(''.join(map(str,digits)))
        digits+=1
        
        return [int(d) for d in str(digits)]
    
obj=Solution()
# digits=[1,2,3]
# digits = [4,3,2,1]
digits=[9]
print(obj.plusOne(digits))
        