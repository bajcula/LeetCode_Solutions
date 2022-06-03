class TwoSum:

    def __init__(self):
        self.nums = []
        self.sorted = False

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.sorted = False

    def find(self, value: int) -> bool:
        if not self.sorted:
            self.nums.sort()
            self.sorted = True
            
        l, r = 0, len(self.nums) - 1
        
        while l < r:
            currSum = self.nums[l] + self.nums[r]  
            if currSum < value:
                l += 1
            elif currSum > value:
                r -= 1
            else:
                return True
            
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)