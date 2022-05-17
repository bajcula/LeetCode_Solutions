class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

#         n1 = len(nums1)
#         n2 = len(nums2)
#         newArr = nums1 + nums2
#         newArr.sort()
        
#         if len(newArr) % 2 == 0:
#             newMedian = (newArr[int((n1 + n2) / 2 - 1)] + newArr[int((n1 + n2) / 2)]) / 2
#             return newMedian
#         else:
#             medianIndex = int((n1 + n2) / 2 - 0.5)
#             return newArr[medianIndex]

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
    
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        
        while True:
            i = (l + r) // 2   #A
            j = half - i - 2   #B
            
            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if i + 1 < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j + 1] if j + 1 < len(B) else float('infinity')
            
            # partition is good
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2:
                    return min(Aright, Bright)
                #even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1