# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head : return head
        a, b = head, head
        currval = a.val
        while b:
            if (b.val != currval):
                a.next = b
                a = b
                currval = a.val
            b = b.next
        a.next = b
        return head
