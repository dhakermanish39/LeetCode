class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        temp=[i+1 for i in range(n+1)]
        for i in nums:
            if i<=n and temp[i]>0:
                temp[i]=-temp[i]
        res=[]
        for i in range(1,len(temp)):
            if temp[i]-1>0:
                res.append(temp[i]-1)
        return res               
        