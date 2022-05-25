class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        
        for i in range(n - 1, -1, -1):            

            if digits[i] != 9:
                
                digits[i] += 1
                
                return digits
                
            else:
                digits[i] = 0
                
        return [1] + digits
    
    
    
#         digits = digits[::-1]
#         remainder = 1
#         i = 0
        
#         while remainder:
#             if i < len(digits):
#                 if digits[i] == 9:
#                     digits[i] = 0
#                 else:
#                     digits[i] += 1
#                     remainder = 0
#             else:
#                 digits.append(1)
#                 remainder = 0
#             i += 1
            
#         return digits[::-1]
        
        