class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        result = []
        l = 0
        r = n - 1

        while l <= r:

            if abs(nums[l]) > abs(nums[r]):
                result.append(nums[l] ** 2)
                l += 1
            else:
                result.append(nums[r] ** 2)
                r -= 1

        return (result[::-1])
        