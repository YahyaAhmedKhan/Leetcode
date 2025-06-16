# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # l = 0
        # curr = head
        # while curr:
        #     curr = curr.next
        #     l+=1

        # mid = l//2-1
        # if l == 1:
        #     return None
        
        # dummy = ListNode()
        # dummy.next = head
        # curr = dummy
        # for i in range(mid+1):
        #     curr = curr.next

        # curr.next = curr.next.next
        # return head

        dummy = ListNode()
        dummy.next = head
        s, f = dummy, dummy
        while f.next and f.next.next:
            f = f.next.next
            s = s.next
        s.next = s.next.next
        return dummy.next

        