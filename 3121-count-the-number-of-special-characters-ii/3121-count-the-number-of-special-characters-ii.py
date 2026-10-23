class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        c=0 
        ans=set()
        for i in range(len(word)):  
            if word[i].isupper():
                
                j=word[i].lower()
                
                if j not in ans and j in word[:i] and j not in word[i+1:]:
                    c+=1
                ans.add(j)    
                        
        return c                



