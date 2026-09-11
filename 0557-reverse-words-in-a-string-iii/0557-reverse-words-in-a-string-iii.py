class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp=s.split()
        ans=[]
        for i in temp:
            ans.append(i[::-1])
        return " ".join(ans)
        