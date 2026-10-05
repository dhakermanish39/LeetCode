class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d={}
        temp=-1
        for i in arr:
            d[i]=d.get(i,0)+1
        for i in d.keys():
            if i==d[i]:
                temp=max(temp,i)
        return temp          
        