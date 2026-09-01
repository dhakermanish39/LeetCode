class Solution(object):

    def maxSubArray(self, nums):
        curr_sum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            maxSum = max(curr_sum, maxSum)
        return maxSum
        