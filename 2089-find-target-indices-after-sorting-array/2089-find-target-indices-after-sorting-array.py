class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        ans=[]
        x=0
        if target in nums:
           x=nums.index(target)
        while x< len(nums) and nums[x]==target:
            ans.append(x)
            x+=1
        return ans    
        