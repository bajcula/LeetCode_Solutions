class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # one line solution
        # return len(set(nums)) != len(nums)

        hashSet = set()
        
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
            
        return False