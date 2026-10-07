class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0
        j=0
        k=0
        res=""
        while i<len(word1) and j<len(word2):
            if k%2==0:
                res+=word1[i]
                i+=1
                if i==len(word1):
                    res+=word2[j:]
                    break
            else:
                res+=word2[j]
                j+=1
                if j == len(word2):
                    res+=word1[i:]   
                    break
            k+=1
        return res            


        