class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        res=0
        temp=0
        for i in divisors:
            c=0
            for j in nums:
                if j%i==0:
                    c+=1
            if c>temp:
                temp=c
                res=i
            elif c==temp:
                res=min(res,i)    
        return res  if res!=0 else   min(divisors)            
    
        