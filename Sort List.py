# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newLinkedList = pointer = ListNode(0) 
        node = head
        stack = []
        while node:
            stack.append(node.val)
            node = node.next
        stack.sort()
        for num in stack:
            pointer.next = ListNode(num)
            pointer = pointer.next
        return newLinkedList.next
