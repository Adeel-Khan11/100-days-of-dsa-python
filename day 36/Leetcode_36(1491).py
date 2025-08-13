class Solution(object):
    def average(self, salary):
        total = 0
        minval = float('inf')
        maxval = float('-inf')

        for s in salary:
            total += s
            minval = min(minval, s)
            maxval = max(maxval, s)

        return (total - minval - maxval) / float(len(salary) - 2)


            
            
            
       
obj=Solution()
# salary = [4000,3000,1000,2000]   
# salary = [1000,2000,3000]
salary=[48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
print(obj.average(salary)) 