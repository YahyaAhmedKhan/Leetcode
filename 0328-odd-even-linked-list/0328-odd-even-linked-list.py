# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        odd = head
        even = head.next
        if not even: return head
        
        o, e = odd, even

        while e.next and e.next.next:
            o.next = o.next.next
            e.next = e.next.next
            o = o.next
            e = e.next
        # print(head)
        # print(o.val, e.val)
        if not e.next:
            o.next = even
            return odd
        else:
            o.next = o.next.next
            o = o.next 
            e.next = None
            o.next = even
            return odd
        
        