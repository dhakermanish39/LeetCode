class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = 0
        for i in range(len(nums)):
           m += nums[i]
           nums[i]=m

        return nums
        