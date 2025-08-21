import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        stones=[-i for i in stones]
        heapq.heapify(stones)
        
        while len(stones)>1:
            max1=-heapq.heappop(stones)
            max2=-heapq.heappop(stones)
            nnum=max1-max2
            
            if nnum!=0:
                heapq.heappush(stones,-nnum)
        if len(stones)==0:
                return 0
        else:
         return -heapq.heappop(stones)
            
obj=Solution()
# stones = [2,7,4,1,8,1]
stones=[1]
print(obj.lastStoneWeight(stones))
           
           
           
           
        