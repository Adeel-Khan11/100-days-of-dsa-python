import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]

        
obj=Solution()
nums = [3,2,1,5,6,4]
k = 2
print(obj.findKthLargest(nums,k))  