class Solution(object):
    def lengthOfLongestSubstring(self, st):
        """
        :type s: str
        :rtype: int
        """
        result=0
        s=[]
        for i in st:
            if i not in s:
                s.append(i)
                
                result=max(result,len(s))
            else:
                
                #result=max(result,len(s))
                while i in s:
                    s.pop(0)
                s.append(i)    
                    
        return result