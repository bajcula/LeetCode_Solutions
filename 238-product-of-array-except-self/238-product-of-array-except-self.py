class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l = len(nums)
        answer = [1] * l
        answer[0] = 1
        
        for i in range(1, l):
            answer[i] = answer[i-1] * nums[i-1]
        
        multiplier = 1
        
        for i in reversed(range(l)):
            answer[i] = answer[i] * multiplier
            multiplier *= nums[i]
            
        return answer