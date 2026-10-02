class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        op = deque()
        result = []

        for i in s:
            if i == "(":
                
               op.append(len(result))
            elif i == ")":
                s =op.pop()
                result[s:] = result[s:][::-1]
            else:
                result.append(i)
        return "".join(result)     
