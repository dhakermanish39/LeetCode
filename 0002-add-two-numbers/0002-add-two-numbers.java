import java.math.BigInteger;
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
     public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        String s1 = "", s2 = "";

        while (l1 != null) {
            
            s1 =   l1.val+s1;
            l1 = l1.next;
        }

        while (l2 != null) {
            s2 =   l2.val+s2;
            l2 = l2.next;
        }
       BigInteger n1 = new BigInteger(s1);
        BigInteger n2 = new BigInteger(s2);

        String res = n1.add(n2).toString();
        
        
       

       
            
        int n=res.length();
        ListNode result = new ListNode (res.charAt(n-1) - '0');
        ListNode re=result;

      for(int i=n-2;i>=0;i--){
          re.next= new ListNode(res.charAt(i) - '0');
          re=re.next;
      }

        
        return result;
    }
}