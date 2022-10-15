# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode(-1)
        list1 = []
        list2 = []
        while l1:
            list1.append(str(l1.val))
            l1 = l1.next
        while l2:
            list2.append(str(l2.val))
            l2 = l2.next
        summ = int(''.join(list1[::-1])) + int(''.join(list2[::-1]))
        temp1 = str(summ)
        num = [int(temp1[i]) for i in range(len(temp1))]
        nums = num[::-1]
        
        for i in nums:
            tail.next = ListNode(i)
            tail = tail.next
        
        return dummy.next
