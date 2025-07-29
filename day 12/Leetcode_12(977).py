class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        index = n - 1

        while left <= right:
            left_val = abs(nums[left])
            right_val = abs(nums[right])
            if left_val > right_val:
                result[index] = left_val * left_val
                left += 1
            else:
                result[index] = right_val * right_val
                right -= 1
            index -= 1  # ✅ Move this outside the if-else block

        return result
