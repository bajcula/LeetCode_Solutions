class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        
        for x, y in points:
            z = (x ** 2) + (y ** 2)
            minHeap.append([z, x, y])
            
        heapq.heapify(minHeap)    
        res = []
        
        for i in range(k):
            z, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
            
        return res