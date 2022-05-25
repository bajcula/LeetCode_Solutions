class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
#         n = len(digits)
        
#         for i in range(n - 1, -1, -1):            
            
#             remainder = 0 if digits[i] != 9 else 1
            
            
            
#             if digits[i] != 9:
#                 digits[i] = digits[i] + remainder
#                 remainder = 0
                
#             else:
#                 digits[i] = 0
#                 remainder = 1
                
#         return digits
    
    
    
        digits = digits[::-1]
        remainder = 1
        i = 0
        
        while remainder:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    remainder = 0
            else:
                digits.append(1)
                remainder = 0
            i += 1
        
        return digits[::-1]
        