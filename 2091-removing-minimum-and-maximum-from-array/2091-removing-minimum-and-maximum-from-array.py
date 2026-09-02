class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        n=len(nums)
        a = min(min_index, max_index)
        b = max(min_index, max_index)

        front = b + 1
        back = n - a
        both = (a + 1) + (n - b)

        return min(front, back, both)