# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node1 =  head
        node2 =  head
        
        i = 0
        while i < n:
            node1 = node1.next
            i += 1
        if node1 is None: return head.next
        
        while node1.next:
            node1 = node1.next
            node2 = node2.next
        node2.next = node2.next.next
        return head
        
