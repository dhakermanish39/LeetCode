class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        s=sum(arr[:k])
        temp=threshold*k
        res=0
        if s>=temp:
            res+=1
        for i in range(k,len(arr)):
            s=s+arr[i]-arr[i-k]
            if s>=temp:
                res+=1
        return res            

        