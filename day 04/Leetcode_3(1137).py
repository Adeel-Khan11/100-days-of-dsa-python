class Solution(object):
    def tribonacci(self, n):
        if(n>=0):
            a,b,c=0,1,1
            for i in range(0,n):
                
                a,b,c=b,c,a+b+c
            return a
        