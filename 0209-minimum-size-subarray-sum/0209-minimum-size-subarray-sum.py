class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        l = s = 0
        ans = n + 1

        for r in range(n):
            s += nums[r]
            while s >= target:
                ans = min(ans, r - l + 1)
                s -= nums[l]
                l += 1

        return 0 if ans == n + 1 else ans