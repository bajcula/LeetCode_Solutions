# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return False
        
        slower = head
        faster = head.next
        
        while slower != faster:
            if faster.next is None or faster.next.next is None:
                return False
            slower = slower.next
            faster = faster.next.next
            
        return True