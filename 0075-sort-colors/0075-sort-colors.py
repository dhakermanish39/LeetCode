class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a=nums.count(0)
        b=nums.count(1)
        c=nums.count(2)
        j=0
        for i in range(a):
            nums[j]=0
            j+=1
        for i in range(b):
            nums[j]=1
            j+=1
        for i in range(c):
            nums[j]=2
            j+=1        
        