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
import java.util.Stack;
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode ans = head;
        ListNode write = head;
        boolean reverse = true;

        ListNode checker = new ListNode(0);
        checker.next = head;
        Stack stack = new Stack();  
        
        while(checker.next != null)
        {for (int i = 0; i<k; i++){
            if (checker.next != null){
                checker = checker.next;
            }
            else reverse = false;
        }
        if (reverse){
            for (int i=0; i<k; i++){
                
                stack.push(head.val);
                head=head.next; 
            }
            for (int i=0; i<k; i++){
                write.val = (int)stack.pop();
                write = write.next;
            }
            
        }}
        
        return ans;
    }
}