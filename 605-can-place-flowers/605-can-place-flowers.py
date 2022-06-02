class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
#         count = 0
        
#         for i in range(len(flowerbed)):

#             if flowerbed[i] == 0:
 
#                 empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
#                 empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
#                 if empty_left_plot and empty_right_lot:
#                     flowerbed[i] = 1
#                     count += 1
#                     if count == n:
#                         return True
                    
#         return count >= n
    
    
        l = len(flowerbed)
        bed = [0] + flowerbed + [0]
        
        for i in range(1, l + 1):
            if bed[i] == bed[i - 1] == bed[i + 1] == 0:
                bed[i] = 1
                n -= 1
            
            if n <= 0: return True
        
        return False