class Solution(object):
    def increasingTriplet(self, nums):
       firstnum=float('inf')
       secondnum=float('inf')
       for i in nums:
        if i<=firstnum:
            firstnum=i
        elif i<=secondnum:
            secondnum=i
        else:
            return True
       return False


  