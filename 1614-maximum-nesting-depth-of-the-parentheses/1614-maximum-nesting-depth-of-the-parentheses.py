class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        temp=0
        for i in s:
            if i=='(':
                temp+=1
                res=max(res,temp)
            elif  i == ')' :
                temp-=1
        return res           

        