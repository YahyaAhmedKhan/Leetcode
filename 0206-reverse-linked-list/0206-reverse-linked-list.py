# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # def rev(node):

        #     if node.next:
        #         ret, first = rev(node.next)
        #         ret.next = node
        #         return node, first
        #     else:
        #         return node, node

        # tail = head
        curr = head
        if not head: return head
        prev = None
        while curr:
            agla = curr.next
            curr.next = prev
            prev = curr
            curr = agla
        return prev
            
        