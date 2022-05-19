class Solution:
    def hammingWeight(self, n: int) -> int:
        
#         counter = 0
        
#         for ch in str(bin(n)):
#             if ch == '1':
#                 counter += 1
                
#         return counter


        return bin(n).count("1")
