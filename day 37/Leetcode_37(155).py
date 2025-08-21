class MinStack(object):
    _stack = []
    _min_stack = []

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val):
        self._stack.append(val)  
        if len(self._min_stack) == 0 or val <= self._min_stack[-1]:
            self._min_stack.append(val)  

    def pop(self):
        if self._stack:
            val = self._stack.pop()
            if val == self._min_stack[-1]:
                self._min_stack.pop()

    def top(self):
        return self._stack[-1]

    def getMin(self):
        return self._min_stack[-1]



minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  
minStack.pop()
print(minStack.top())     
print(minStack.getMin())  


