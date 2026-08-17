class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = 0
        num = []

        for i in nums:
           m += i
           num.append(m)

        return num
        