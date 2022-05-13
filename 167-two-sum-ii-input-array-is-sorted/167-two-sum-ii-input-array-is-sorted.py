class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        length = len(numbers)
        l = 0
        r = length - 1
        total = 0
        
        while l <= r:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l + 1, r + 1]