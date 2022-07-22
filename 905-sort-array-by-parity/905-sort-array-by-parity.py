class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        res = []
        for num in nums:
            if num % 2 == 1:
                res.append(num)
            else:
                res.insert(0, num)
        
        return res