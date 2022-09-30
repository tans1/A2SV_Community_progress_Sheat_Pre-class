# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        node = head
        prev = dummy
        while node:
            while node.next and node.val == node.next.val:
                node = node.next
            if prev.next == node:
                prev = prev.next 
                node = node.next
            else:
                prev.next = node.next
                node = prev.next
                
        return dummy.next
