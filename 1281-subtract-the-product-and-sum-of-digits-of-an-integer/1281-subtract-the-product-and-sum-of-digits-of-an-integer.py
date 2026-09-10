class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        m=1
        while n>0:
            temp=n%10
            s+=temp
            m*=temp
            n=n//10
        return m-s    
        