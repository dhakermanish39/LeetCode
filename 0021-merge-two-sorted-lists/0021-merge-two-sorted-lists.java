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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
 
        ListNode temp1=list1;
        ListNode temp2 =list2;
        if(temp1 == null && temp2 == null){
        
         return null;
        }
        int x=0;
        
        
          if(temp1 != null) {
                if(temp2 ==null || (temp1.val < temp2.val)){
                   x=temp1.val;
                    temp1=temp1.next;
                }
                else{
                     x=temp2.val;
                    temp2=temp2.next;
                }
            }
            else if(temp2!=null){
                   x=temp2.val;
                    temp2=temp2.next;
            }

        
        ListNode result = new ListNode(x);
                 ListNode temp =result;

        while(temp1!=null || temp2 != null){
            if(temp1 != null) {
                if(temp2 ==null || (temp1.val < temp2.val)){
                    temp.next=new ListNode(temp1.val);
                     
                    temp=temp.next;
                    temp1=temp1.next;
                }
                else{
                     temp.next=new ListNode(temp2.val);
                    temp=temp.next;
                    temp2=temp2.next;
                }
            }
            else{
                   temp.next=new ListNode(temp2.val);
                 
                    temp=temp.next;
                    temp2=temp2.next;
            }

        }
        return result;
        
    }
}