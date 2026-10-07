class Solution(object):
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])
        length = m + n - 1
        if length % 2 != 0:
            return False

        if grid[0][0] == ')':
            return False
        if grid[m - 1][n - 1] == '(':
            return False
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)
        for i in range(m):
            for j in range(n):
                for balance in dp[i][j]:
                    if i + 1 < m:
                        if grid[i + 1][j] == '(':
                            new_balance = balance + 1
                        else:
                            new_balance = balance - 1

                        if new_balance >= 0:
                            dp[i + 1][j].add(new_balance)
                    if j + 1 < n:
                        if grid[i][j + 1] == '(':
                            new_balance = balance + 1
                        else:
                            new_balance = balance - 1
                        if new_balance >= 0:
                            dp[i][j + 1].add(new_balance)

        return 0 in dp[m - 1][n - 1]