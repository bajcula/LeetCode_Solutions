class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        while n:
            if n == 1: 
                return True
            
            if n % 3 == 0:
                n = n / 3
                
            else:
                return False