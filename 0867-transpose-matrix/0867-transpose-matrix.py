class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])

        ans = []

        for j in range(cols):
            temp = []
            for i in range(rows):
                temp.append(matrix[i][j])
            ans.append(temp)

        return ans