class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        x = 0
        
        for string in operations:
            if string == '--X' or string == 'X--':
                x -= 1
            else:
                x += 1
                
        return x