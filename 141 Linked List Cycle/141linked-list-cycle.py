# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s= set()
        curr = head
        if not head: return False
        curr2 = head.next
        if not (curr and curr2): return False

        while curr2 and curr:
            if curr == curr2: return True
            curr = curr.next
            curr2 = curr2.next
            if not curr2: return False
            curr2 = curr2.next
        
        return False