class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        a="abcdefghijklmnopqrstuvwxyz"
        for i in a:
            if i not in sentence:
                return False
        return True        
        