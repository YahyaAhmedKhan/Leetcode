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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode t = head;
        if (head==null) return head;
        int sz = 1;
        while (t.next!= null){
            t = t.next;
            sz++;
        }
        n = sz-n;
        if (n == 0) return head.next;
        t = head;
        while (--n > 0) t = t.next;
        t.next = t.next.next;
        return head;
    }
}