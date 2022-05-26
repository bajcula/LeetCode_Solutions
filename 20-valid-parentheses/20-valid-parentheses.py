class Solution:
    def isValid(self, s: str) -> bool:
        
        helper = []
        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        
        for char in s:
            if char in pairs:
                if helper and helper[len(helper) - 1] == pairs[char]:
                    helper.pop()
                else:
                    return False
            else:
                helper.append(char)
                
        return True if not helper else False
        