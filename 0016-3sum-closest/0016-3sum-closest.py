class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j <k:
                
                total = nums[i] + nums[j] + nums[k]

                if abs(total - target) < abs(ans- target):
                    ans = total
                
                if total == target:
                    return total
                elif total < target:
                    j+=1
                else:
                    k-=1
        return ans
 