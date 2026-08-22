class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        """
        r=0
        for i in wordDict:
            if i not in s:
                return False
            r+=len(i)    
        return  True  if len(s)>=r else False
        """
        result = [False for i in range(len(s))]
        wd = set(wordDict)
        for i in range (len(s)):
            if s[:i+1] in wd:
                result[i] = True
                continue
            for j in range(i-1, -1, -1):
                if result[j]:
                
                    if s[j+1:i+1] in wd:
                        result[i] = True
                        break
     
        return result[-1]