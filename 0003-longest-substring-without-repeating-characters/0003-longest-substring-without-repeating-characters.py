class Solution(object):
    def lengthOfLongestSubstring(self, st):
        """
        :type s: str
        :rtype: int
        """
        count=0
        result=0
        s=[]
        for i in st:
            if i not in s:
                s.append(i)
                count+=1
                result=max(result,count)
            else:
                
                result=max(result,len(s))
                while i in s:
                    s.pop(0)
                    count-=1
                s.append(i)  
                count+=1  
                    
        return result