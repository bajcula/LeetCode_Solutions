class Solution:
    def hammingWeight(self, n: int) -> int:
        
        counter = 0
        nStr = str(bin(n))
        
        for ch in nStr:
            if ch == '1':
                counter += 1
                
        return counter