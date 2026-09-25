class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n=len(matrix)
        m=len(matrix[0])
        k=0
      
        ans=[]
        while k<n and k<m:
            for i in range(k,m):
                ans.append(matrix[k][i])
            for i in range(k+1,n):
                ans.append(matrix[i][m-1])
            if k<n-1:
                for i in range(m-2,k,-1):
                    ans.append(matrix[n-1][i])
            if k<m-1:        
                for i in range(n-1,k,-1):
                    ans.append(matrix[i][k])
            k+=1
            n-=1
            m-=1    

        return ans              
            
        