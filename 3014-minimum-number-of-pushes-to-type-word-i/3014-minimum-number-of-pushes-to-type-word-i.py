class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        if len(word)<= 8:
            return len(word)
        if len(word)//8==1:
            return 8+ (len(word)%8)*2
        if len(word)//8==2:
            return 24+ (len(word)%8)*3
        if len(word)//8==3:
            return 48+ (len(word)%8)*4    

          
        
        