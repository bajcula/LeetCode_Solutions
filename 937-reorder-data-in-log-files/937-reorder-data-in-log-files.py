class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def sort(log):
            
            first_part, second_part = log.split(" ", maxsplit = 1)
            return (0, second_part, first_part) if second_part[0].isalpha() else (1, )
        
        return sorted(logs, key = sort)