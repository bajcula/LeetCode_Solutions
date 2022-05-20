class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        helper = ""
        
        for char in s:
            if char.isalnum():
                helper += char.lower()
            
        return helper == helper[::-1]
        