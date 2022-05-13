class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashMap = {}
        output = []
        
        for num in nums:
            hashMap[num] = 1
            
        for num in range(1, len(nums) + 1):
            if num not in hashMap:
                output.append(num)
        
        return output
    
    