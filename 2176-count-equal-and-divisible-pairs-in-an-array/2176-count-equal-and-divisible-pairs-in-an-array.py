class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        output = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    output += 1
                    
        return output