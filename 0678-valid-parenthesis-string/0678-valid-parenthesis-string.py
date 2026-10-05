class Solution(object):
    def checkValidString(self, s):
        lst=[]
        star=[]
        for i in range(len(s)):
            if s[i]=='(':
                lst.append(i)
            elif s[i]=='*':
                star.append(i)
            else:
                if lst:
                    lst.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while lst and star:
            if lst[-1]<star[-1]:
                lst.pop()
                star.pop()
            else:
                return False
        return len(lst)==0