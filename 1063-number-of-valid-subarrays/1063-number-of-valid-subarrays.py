class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
        stack = []
        res = 0
        
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                pre_idx = stack.pop()
                res += i - pre_idx
            stack.append(i)
                
        while stack:
            idx = stack.pop()
            res += n - idx
            
        return res