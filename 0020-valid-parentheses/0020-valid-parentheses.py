class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[]
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if not st:
                    return False
                else:
                    
                    j=st.pop()
                if pairs[i]!=j:
                    return False
                
        return True if len(st)==0 else False               

