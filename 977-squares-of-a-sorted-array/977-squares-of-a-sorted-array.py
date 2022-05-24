class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = []
        l = 0
        r = n - 1

        while l <= r:

            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l] ** 2)
                l += 1
            else:
                res.append(nums[r] ** 2)
                r -= 1

        return (res[::-1])
        