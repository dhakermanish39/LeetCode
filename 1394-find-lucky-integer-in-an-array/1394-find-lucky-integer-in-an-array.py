class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d={}
        temp=[]
        for i in arr:
            d[i]=d.get(i,0)+1
        for i in d.keys():
            if i==d[i]:
                temp.append(i)
        return max(temp) if temp else -1            
        