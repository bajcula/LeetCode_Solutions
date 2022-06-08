class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
            
#         for i in range(len(nums)):
#             nums[i] = nums[nums[i]]
            
#         return nums


        n = len(nums)
        for i in range(n):
            
            r = nums[i]
            b = nums[nums[i]] % n
            nums[i] = n * b + r
            
        for i in range(len(nums)):
            nums[i] = nums[i] // n
            
        return nums
        