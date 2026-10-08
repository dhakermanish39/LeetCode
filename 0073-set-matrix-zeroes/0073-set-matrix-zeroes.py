class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=[]
        cln=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.append(i)
                    cln.append(j)
        for temp in range(len(row)):
            for i in range(n):
                matrix[row[temp]][i]=0            
        for temp in range(len(cln)):
            for i in range(m):
                matrix[i][cln[temp]]=0           



        