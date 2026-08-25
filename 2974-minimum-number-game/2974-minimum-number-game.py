class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[]
        nums.sort()
        i=0
        while i < len(nums):
            arr.append(nums[i+1])
            arr.append(nums[i])
            i+=2
        return arr    
        