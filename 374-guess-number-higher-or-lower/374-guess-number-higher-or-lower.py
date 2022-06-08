# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        low, high = 1, n
        
        while True:
            
            num = low + (high - low) // 2
            g = guess(num)
            
            if g == -1:
                high = num - 1
            elif g == 1:
                low = num + 1
            else:
                return num