class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        words.reverse()
        result=" ".join(words)
        return result
        