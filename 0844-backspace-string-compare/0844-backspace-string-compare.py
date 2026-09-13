class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        temp1=[]
        temp2=[]
        for i in s:
            if i =='#':
                if temp1:
                    temp1.pop()
            else:
                temp1.append(i)
        for i in t:
            if i =='#':
                if temp2:
                    temp2.pop()
            else:
                temp2.append(i)     
        return temp1==temp2           

        