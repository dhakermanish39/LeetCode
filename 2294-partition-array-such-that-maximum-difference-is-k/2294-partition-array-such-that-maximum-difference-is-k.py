class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        count = 1
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - start > k:
                count += 1
                start = nums[i]

        return count