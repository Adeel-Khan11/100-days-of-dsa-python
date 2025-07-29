class Solution(object):
    def searchRange(self, nums, target):
        def binarySearch(findFirst):
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    if findFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        first = binarySearch(True)
        last = binarySearch(False)
        return [first, last]

obj=Solution()
# nums=[5,7,7,8,8,10]
nums=[]
target=0
print(obj.searchRange(nums,target))
                
            
            
            
            
            
        