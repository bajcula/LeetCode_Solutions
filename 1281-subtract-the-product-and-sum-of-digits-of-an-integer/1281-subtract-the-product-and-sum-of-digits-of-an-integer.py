class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        prodDig = 1
        sumDig = 0
        
        for char in str(n):
            prodDig *= int(char)
            sumDig += int(char)
            
        return prodDig - sumDig