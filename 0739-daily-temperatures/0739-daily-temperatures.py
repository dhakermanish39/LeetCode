class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans=[0]*n
        s=[]
        for i in range(n):
            while s and temperatures[i] > temperatures[s[-1]]:
                j=s.pop()
                ans[j]=i - j
            s.append(i)
        return ans