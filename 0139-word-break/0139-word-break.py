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
        dp = [False for i in range(len(s)+1)]
        dp[0] = True

        wordDict = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]