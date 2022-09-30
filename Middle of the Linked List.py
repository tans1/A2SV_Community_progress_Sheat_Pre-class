# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        i = 0
        while head:
            i +=1
            head = head.next
        j = 0
        while node:
            if j == i//2:
                return node
            j +=1
            node = node.next
        return None
