class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        richest = 0
        
        for row in accounts:
            total = 0
            for amount in row:
                total += amount
                
            richest = max(richest, total)
                
        return richest