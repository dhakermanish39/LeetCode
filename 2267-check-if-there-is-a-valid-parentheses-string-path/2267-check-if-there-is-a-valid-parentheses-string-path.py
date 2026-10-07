class Solution(object):
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        length = m + n - 1

        if length % 2 == 1:
            return False

        memo = {}

        def dfs(i, j, balance):
            if balance < 0:
                return False

            if balance > length:
                return False

            if i == m - 1 and j == n - 1:
                return balance == 0

            key = (i, j, balance)

            if key in memo:
                return memo[key]

            if i + 1 < m:
                if grid[i + 1][j] == '(':
                    new_balance = balance + 1
                else:
                    new_balance = balance - 1

                if dfs(i + 1, j, new_balance):
                    memo[key] = True
                    return True

            if j + 1 < n:
                if grid[i][j + 1] == '(':
                    new_balance = balance + 1
                else:
                    new_balance = balance - 1

                if dfs(i, j + 1, new_balance):
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return dfs(0, 0, 1)