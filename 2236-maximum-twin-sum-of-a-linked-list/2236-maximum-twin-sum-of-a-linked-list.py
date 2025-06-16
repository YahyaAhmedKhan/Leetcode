# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        curr = head
        n = 0
        while curr:
            n+=1
            curr = curr.next
        
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        vals = []
        for i in range(n//2):
            curr = curr.next
            vals.append(curr.val)

        j = len(vals)
        maxi = -1
        for i in range(n//2):
            curr = curr.next
            j-=1
            maxi =max (maxi, vals[j]+curr.val)

        return maxi

        

        