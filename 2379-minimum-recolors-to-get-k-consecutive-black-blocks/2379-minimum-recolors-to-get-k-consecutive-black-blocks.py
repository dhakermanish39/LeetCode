class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        c=blocks[:k].count('W')
        temp=c
        for i in range(k,len(blocks)):
            if blocks[i]=='W':
                temp+=1
            if blocks[i-k]=='W':
                temp-=1
            c=min(c,temp)
        return c            
        
        