class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        sub = []
        
        def dfs(i):
            if i == len(nums):
                output.append(sub.copy())
                return
            
            sub.append(nums[i])
            dfs(i + 1)
            
            sub.pop()
            dfs(i + 1)
            
        dfs(0)
        return output