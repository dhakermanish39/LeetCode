class Solution(object):
    def longestValidParentheses(self, s):
        res=0
        st=[-1]
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    res=max(res, i - st[-1])
                    
        return res