class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
      
        c=1
        if nums[0]%k==0:
            if nums[0]//k==c:
                c+=1
            else:
                return k*c    
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1] and nums[i]%k==0:
                if nums[i]//k==c:
                    c+=1
                else :
                    
                    return k*c
                    
        return k*c           
                    
        