class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        doubles = {}
        
        for num in nums:
            doubles[num] = doubles.get(num, 0) + 1
      
        for key, val in doubles.items():
            if val == 1:
                return key