# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        c = 0
        curr = head
        tail = head
        while curr:
            c+=1 
            if not curr.next:
                tail = curr
            curr = curr.next
        tail.next = ListNode()
        
            
        def show(node):
            curr = node
            while curr:
                print(curr.val, end="->")
                curr = curr.next

        for i in range(c):
            pre_node = dummy
            for j in range(i):
                pre_node = pre_node.next
            node = pre_node.next
            pre_node.next = node.next

            pre_pos = dummy
            pre_pos.val = float("-inf")
            cc = pre_pos
            for k in range(i+1):
                if cc.val<=node.val:
                    pre_pos = cc
                else: break
                cc = cc.next

            node.next = pre_pos.next
            pre_pos.next = node
            # show(dummy.next)
            # print(i)

        curr_ = dummy
        while curr_.next.next:
            curr_ = curr_.next
        curr_.next = None
        return dummy.next

    

        