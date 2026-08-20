class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result=[]
        for i in range(len(matrix)):
            result.append(len(matrix[i])-matrix[i].count(0))
        return result    


        