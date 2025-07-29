class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
      if 1 <= numBottles <= 100 and 1 <= numExchange <= 100:
          total=numBottles
          while (numBottles >= numExchange):
              mod=numBottles//numExchange
              rem=numBottles%numExchange
              total=total+mod
              numBottles=mod+rem
          return total
sc=Solution()
sc.numWaterBottles(9,3)
              
              
              