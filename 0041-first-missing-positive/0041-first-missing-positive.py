class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n:
                correct = nums[i] - 1

                if nums[i] == nums[correct]:
                    break

                nums[i], nums[correct] = nums[correct], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1