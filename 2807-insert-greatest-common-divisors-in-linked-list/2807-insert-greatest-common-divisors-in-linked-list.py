# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        if head.next is None or head is None :
            return head
        temp =head
        while temp.next is not None:
            v1=temp.val
            v2=temp.next.val
            v3= ListNode(gcd(v1, v2)) 
            temp1=temp.next
            temp.next=v3
            v3.next=temp1
            temp=temp.next.next
        return head    
