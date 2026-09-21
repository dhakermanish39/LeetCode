class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        temp=sum(nums[:k])
        s=temp
        for i in range(k,len(nums)):
            temp=temp+nums[i]
            temp=temp-nums[i-k]
            s=max(s,temp)
        return float(s)/k    
        