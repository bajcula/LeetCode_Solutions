# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        arr = []
        curr = head
        maxSum = 0
        
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        n = len(arr)
        for i in range(n):
            currSum = arr[i] + arr[n - i - 1]
            maxSum = max(currSum, maxSum)
            
        return maxSum