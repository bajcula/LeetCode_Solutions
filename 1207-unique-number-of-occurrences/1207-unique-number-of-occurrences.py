class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        hashMap = {}
        
        for item in arr:
            if item in hashMap:
                hashMap[item] += 1
            else:
                hashMap[item] = 1
                
        unique = set(hashMap.values())
                
        return len(unique) == len(hashMap)
        