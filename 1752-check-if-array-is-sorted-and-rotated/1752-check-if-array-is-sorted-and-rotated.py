class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans=0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                ans =i
                break
        return sorted(nums)==nums[ans:]+nums[:ans]        

        