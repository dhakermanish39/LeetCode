class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        """
        d = {chr(i): False for i in range(ord('a'), ord('z') + 1)}
        d1 = {chr(i): False for i in range(ord('A'), ord('Z') + 1)}
        for i in word:
            if i.isupper():
                d1[i]=True
            elif i.islower():
                d[i]=True
        c=0
        for i in d.keys():
            j=i.upper()
            if d[i] and d1[j]:
                c+=1
        return c """ 
        c=0 
        ans=set()
        for i in range(len(word)):  
            if word[i].isupper():
                
                j=word[i].lower()
                
                if j not in ans and j in word[:i] and j not in word[i+1:]:
                    c+=1
                ans.add(j)    
                        
        return c                



