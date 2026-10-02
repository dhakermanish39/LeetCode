class Solution(object):
    def characterReplacement(self, s, k):
        m=0
        l=0
        mp={}
        mx=0

        for r in range(len(s)):
            mp[s[r]]=mp.get(s[r],0)+1

            mx=max(mx,mp[s[r]])

            while (r-l+1)-mx>k:
                mp[s[l]]-=1
                l+=1

            m=max(m,r-l+1)

        return m