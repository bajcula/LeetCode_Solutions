class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
    
        n = len(nums)
        res = []
        currSum = sum(nums)
        
        totalMissing = int(n * (n + 1) / 2 - currSum)
        duplicateNum = currSum - sum(set(nums))
   
        return [duplicateNum, duplicateNum + totalMissing]