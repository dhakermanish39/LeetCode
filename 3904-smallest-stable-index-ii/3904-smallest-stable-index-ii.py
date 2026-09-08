class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0 if k >= 0 else -1

        mn = [0] * len(nums)
        mn[-1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            mn[i] = min(nums[i], mn[i + 1])

        m = nums[0]

        for i in range(len(nums)):
            if nums[i] > m:
                m = nums[i]

            if m - mn[i] <= k:
                return i

        return -1