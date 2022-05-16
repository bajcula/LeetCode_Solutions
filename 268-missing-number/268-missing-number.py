class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
#         numSet = set(nums)
        
#         for num in range(len(nums) + 1):
#             if num not in numSet:
#                 return num

        
        sumNums = 0
        sumAllNums = 0
    
        for num in range(len(nums) + 1):
            sumAllNums += num
            
        for num in nums:
            sumNums += num
            
        return sumAllNums - sumNums