class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        if len(nums)==len(set(nums)):
            return 0
        c=0
        n=len(nums)
        x=0
        while c<n:
            if len(nums)==len(set(nums)):
                return x
            if c <n:
                nums.pop(0) 
                c+=1
            if c<n:
                nums.pop(0)
                c+=1
            if c<n:
                nums.pop(0) 
                c+=1
            x+=1
        return x         
        """
        result=-1
        if len(nums)==len(set(nums)):
            return 0
        s=set()  
        for i in range(len(nums)-1,-1,-1):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                result=i
                break   
        return (result//3) +1        



            
        