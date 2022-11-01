# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = ListNode(head.val, head.next)
        while head.next!= None:
            slow = slow.next
            if head.next.next != None:
                head = head.next.next
                continue
            head = head.next
        return slow
        
