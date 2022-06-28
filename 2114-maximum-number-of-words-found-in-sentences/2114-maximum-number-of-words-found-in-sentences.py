class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        maxWords = 0
        
        for sen in sentences:
            
            maxWords = max(maxWords, len(sen.split(" ")))
        
        return maxWords