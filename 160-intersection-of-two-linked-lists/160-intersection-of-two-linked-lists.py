# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        def getCount(node):
        
            curr = node
            count = 0

            while curr is not None:
                count += 1
                curr = curr.next

            return count

        
        def getTheNode(diff, head1, head2):
        
            curr1 = head1
            curr2 = head2

            for i in range(diff):
                if curr1 is None:
                    return -1
                curr1 = curr1.next

            while curr1 is not None and curr2 is not None:
                if curr1 is curr2:
                    return curr1

                curr1 = curr1.next
                curr2 = curr2.next

            return None
        
        
        a = getCount(headA)
        b = getCount(headB)
        
        if a < b:
            a, b = b, a
            headA, headB = headB, headA
        
        diff = a - b
        
        return getTheNode(diff, headA, headB)