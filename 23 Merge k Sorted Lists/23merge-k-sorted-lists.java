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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length==1) return lists[0];
        if (lists.length==0) return null;
        ListNode ans = null;
        int m=0;
        for (int i=0; i<lists.length; i++){
            if (lists[i]!=null){
                if (ans==null){
                    ans = lists[i];
                    m = i;
                }
                else{
                    if (lists[i].val<ans.val){
                        ans = lists[i];
                        m = i;
                    }
                }
            }
        }
        int min1=0;
            ListNode checkerNode1=null;
            for (int i=0; i<lists.length; i++){
                if (lists[i]!=null){
                    checkerNode1 = lists[i];
                    min1 = i;
                    break;
                }
            }
            if (checkerNode1==null) return ans;
        lists[m] = lists[m].next;
        ListNode n = ans;
        while(true){
            int min=0;
            ListNode checkerNode=null;
            for (int i=0; i<lists.length; i++){
                if (lists[i]!=null){
                    checkerNode = lists[i];
                    min = i;
                    break;
                }
            }
            if (checkerNode==null) return ans;
            
            for (int i=0; i<lists.length; i++){
                if (lists[i]!=null){
                    if (lists[i].val<lists[min].val) min = i;
                }
            }
            n.next = lists[min];
            n = n.next;
            lists[min] = lists[min].next; 
        }
    }
}