class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        result = 0
        boxTypes.sort(key=lambda x: -x[1])
        i = 0
        
        while truckSize > 0 and i < len(boxTypes):
            
            if (truckSize > boxTypes[i][0]):
                result += boxTypes[i][0] * boxTypes[i][1]
            else:
                result += truckSize * boxTypes[i][1]
                return result
          
            truckSize -= boxTypes[i][0]
            i += 1
            
        return result
            
        