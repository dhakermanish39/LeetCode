class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        x=1
        while x<n:
            x=x*4
            if x==n:
                return True
        return False        
            
        