class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        ans=0
        for i in nums:
            if i==0:
                c=0
            else:
                c+=1
                ans=max(ans,c)    
        return ans        