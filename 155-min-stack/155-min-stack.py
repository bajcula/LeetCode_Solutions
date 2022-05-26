class MinStack:

    def __init__(self):
        self.stack = []
        self.helpStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.helpStack:
            val = min(val, self.helpStack[-1])
        self.helpStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.helpStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.helpStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


