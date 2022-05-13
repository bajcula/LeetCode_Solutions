class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n1 = len(nums1)
        n2 = len(nums2)
        newArr = nums1 + nums2
        newArr.sort()
        
        if len(newArr) % 2 == 0:
            newMedian = (newArr[int((n1 + n2) / 2 - 1)] + newArr[int((n1 + n2) / 2)]) / 2
            return newMedian
        else:
            medianIndex = int((n1 + n2) / 2 - 0.5)
            return newArr[medianIndex]