class MyStack(object):
    
    

    def __init__(self):
        self.stack=[]
        self.checkstack=[]
        
        

    def push(self, x):
        self.stack.append(x)
        self.checkstack.append(x)
        
        

    def pop(self):
       if self.stack:
        return self.stack.pop()
       else:
        return None  # or raise an error

        

    def top(self):
     if self.stack:
        return self.stack[-1]

        

    def empty(self):
     return len(self.stack) == 0

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()