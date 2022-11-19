class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
    
        n = len(nums)
        res = []
        currSum = sum(nums)
        setSum = sum(set(nums))
        
        totalMissing = int(n * (n + 1) / 2 - currSum)
        duplicateNum = currSum - setSum
   
        return [duplicateNum, duplicateNum + totalMissing]