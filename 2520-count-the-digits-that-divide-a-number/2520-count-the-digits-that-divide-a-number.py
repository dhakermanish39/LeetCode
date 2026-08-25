class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        x=num
        c=0
        while x>0:
            temp=x%10
            x=x//10
            if num % temp==0:
                c+=1
        return c        
        