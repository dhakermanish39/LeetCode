class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x=n
        s,m=0,1

        while x>0:
            temp=x%10
            x=x//10
            s+=temp
            m*=temp
        s=s+m    
        return n%s==0     
        