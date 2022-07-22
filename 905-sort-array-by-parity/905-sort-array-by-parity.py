class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
#         res = []
#         for num in nums:
#             if num % 2 == 1:
#                 res.append(num)
#             else:
#                 res.insert(0, num)
        
#         return res

        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] % 2 == 0:
                l += 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                
        return nums