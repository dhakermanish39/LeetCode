class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        a=[]
        for i in nums:
            if i%2==0:
                ans.append(i)
            else:
                a.append(i)
        return ans+a            

        