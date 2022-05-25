class Solution:
    def isHappy(self, n: int) -> bool:
        
        slow = n
        fast = self.squareSum(n)
        
        while slow != fast:
            fast = self.squareSum(fast)
            fast = self.squareSum(fast)
            slow = self.squareSum(slow)

        return fast == 1 
         
    def squareSum(self, n):
        
        res = 0
        
        while n:
            res += (n % 10) ** 2
            n = n // 10
            
        return res