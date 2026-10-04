class Solution(object):
    def totalFruit(self, a):
        i=0
        d={}
        maxlen=0
        for j in range(0,len(a)):
            if a[j] in d:
                d[a[j]]+=1
            else:
                d[a[j]]=1
            while len(d)>2:
                d[a[i]]-=1
                if d[a[i]]==0:
                    del d[a[i]]
                i+=1
            maxlen=max(maxlen,j-i+1)
        return maxlen
        