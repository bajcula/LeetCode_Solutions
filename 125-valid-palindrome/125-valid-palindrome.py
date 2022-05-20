class Solution:
    def isPalindrome(self, s: str) -> bool:
        
#         helper = ""
        
#         for char in s:
#             if char.isalnum():
#                 helper += char.lower()
            
#         return helper == helper[::-1]
        
    
        l = 0
        r = len(s) - 1
        
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True