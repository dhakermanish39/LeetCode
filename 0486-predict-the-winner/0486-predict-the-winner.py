class Solution:
    def predictTheWinner(self, nums):
        n = len(nums)
        dp = {}
        def solve(i, j):
            if i == j:
                return nums[i]
            if (i, j) in dp:
                return dp[(i, j)]
            left = nums[i] - solve(i + 1, j)
            right = nums[j] - solve(i, j - 1)
            dp[(i, j)] = max(left, right)
            return dp[(i, j)]
        return solve(0, n - 1) >= 0