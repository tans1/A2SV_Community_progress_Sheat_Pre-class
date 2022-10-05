# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        prev  = ListNode()
        curr = head.next
        
        while head and head.next:
            temp = head.next 
            head.next = temp.next
            temp.next = head
            prev.next = temp
            head = head.next
            prev = temp.next
        return curr

            
