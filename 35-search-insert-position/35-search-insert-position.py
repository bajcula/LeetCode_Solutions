class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            
            pivot = (l + r) // 2
            
            if nums[pivot] == target:
                return pivot
                
            elif nums[pivot] < target:
                l = pivot + 1
                
            elif nums[pivot] > target:
                r = pivot - 1
                
        return l