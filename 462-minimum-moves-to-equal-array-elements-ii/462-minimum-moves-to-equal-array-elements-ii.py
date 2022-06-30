class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        nums.sort()
        
        counter = 0
        
        for num in nums:
            counter += round(abs(num - nums[len(nums) // 2]))
            
        return counter