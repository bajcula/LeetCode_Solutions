class Solution:
    def minimumSum(self, num: int) -> int:
        
        digits = [int(d) for d in str(num)]
        
        digits.sort()
        
        return digits[0] * 10 + digits[1] * 10 + digits[2] + digits[3]