class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        sm=0    
        for i in d.keys():
            if d[i]==1:
                sm+=i
        return sm            