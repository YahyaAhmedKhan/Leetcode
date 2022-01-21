/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode node = head;
        if(head== null) return head;
        if (head.next==null) return head;
        boolean swap = true;
        int temp = 0;
        while(node.next != null){
            if(swap){
                temp = node.val;
                node.val=node.next.val;
                node.next.val = temp;
            }
            swap = !swap;
            node=node.next;
        }
        return head;
    }
}