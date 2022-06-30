class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        res = 0
        
        for idx, num in enumerate(nums):
            for j in range(idx + 1, len(nums)):
                if num == nums[j]:
                    res += 1
                    
        return res