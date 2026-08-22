# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        
        if head is None or left == right:
            return head

        temp = ListNode(0)
        temp.next = head

        prev = temp

        for i in range(1, left):
            prev = prev.next

        curr = prev.next

        for i in range(right - left):
            next_node = curr.next

            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return temp.next