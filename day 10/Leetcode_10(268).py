class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total = (n * (n + 1)) // 2
        return total - sum(nums)

obj = Solution()
num1 = [1, 8]
print(obj.missingNumber(num1))
