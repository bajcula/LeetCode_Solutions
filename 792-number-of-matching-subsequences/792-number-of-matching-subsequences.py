class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        count = 0
        
        state = defaultdict(list)
        
        for word in words:
            state[word[0]].append(word[1:])
            
        for char in s:
            old_bucket = state[char]
            state[char] = []
            
            for suffix in old_bucket:
                if not suffix:
                    count += 1
                else:
                    state[suffix[0]].append(suffix[1:])
                    
        return count