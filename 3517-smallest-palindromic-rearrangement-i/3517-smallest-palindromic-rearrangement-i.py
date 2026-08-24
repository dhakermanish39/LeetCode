class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)%2==0:
            a=s[:len(s)//2]
            a=sorted(a)
            a="".join(map(str,a))
            a=a+a[::-1]
        else:
            a=s[:len(s)//2]
            a=sorted(a)
            a="".join(map(str,a))
            a=a+s[len(s)//2]+a[::-1]
        return a    
        
         
        