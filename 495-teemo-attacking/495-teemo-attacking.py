class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        total = duration
        n = len(timeSeries)
        
        for i in range(1, n):
            
            total += min(timeSeries[i] - timeSeries[i - 1], duration)
            
        return total