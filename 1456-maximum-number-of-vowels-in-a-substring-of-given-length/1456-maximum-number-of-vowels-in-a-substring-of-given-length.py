class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res=0
        for i in range(k):
            if s[i] in "aeiou":
                res+=1
        temp =res
        for i in range(k,len(s)):
            if s[i-k] in "aeiou":
                temp-=1
            if  s[i] in "aeiou":
                temp+=1
            res=max(res,temp)
        return res                  
        