class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        N=len(arr)
        i=0
        while i<N:
            if arr[i]==0:
               arr.pop(N-1)
               arr.insert(i,0)
               i+=1
            i+=1    
        