class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        for i in range(1,len(nums)):
            if nums[i]-1!=nums[i-1]:
                break
            count+=1
        ps=sum(nums[:count])
        while True:
            if ps not in nums:
                return ps
            ps+=1                 


        