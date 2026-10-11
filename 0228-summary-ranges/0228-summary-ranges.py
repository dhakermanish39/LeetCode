class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        
        res =[]
        s=0
        e=0
        n=len(nums)
        for i in range(1,len(nums)):
            if nums[i]-1!=nums[i-1]:
                e=nums[i-1]
                if e==s:
                    res.append(str(s))
                else:
                    res.append(str(s)+"->"+str(e))
                s=nums[i]

        if s==nums[-1]:
            res.append(str(s))    
        else:
            res.append(str(s)+"->"+str(nums[n-1]))

        return res   
        """
        result = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            end = nums[i]

            if start == end:
                result.append(str(start))
            else:
                result.append(str(start)+"->"+str(end))

            i += 1

        return result
             

        