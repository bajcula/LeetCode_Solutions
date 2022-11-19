class MRUQueue:

    def __init__(self, n: int):
        self.data = list(range(1, n+1))

    def fetch(self, k: int) -> int:
        
        temp = self.data.pop(k - 1)
        self.data.append(temp)
 
        return self.data[len(self.data) - 1]

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)