class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def signFun(x):
            if x==0:
                return 0
            return 1 if x>0 else -1
        n=1
        for i in nums:
            n*=i
        return signFun(n)            
        