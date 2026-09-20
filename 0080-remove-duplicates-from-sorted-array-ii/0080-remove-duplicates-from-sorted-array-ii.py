class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=1
        temp=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]  :
                temp+=1
            else:
                temp=1
            if temp<3:
                nums[k]=nums[i]
                k+=1
           
        return k              

        