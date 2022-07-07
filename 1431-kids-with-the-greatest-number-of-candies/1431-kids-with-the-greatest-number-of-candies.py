class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maximum = candies[0]
        
        for can in candies:
            maximum = max(maximum, can)
            
        output = []
        
        for can in candies:
            output.append(can + extraCandies >= maximum)
            
        return output