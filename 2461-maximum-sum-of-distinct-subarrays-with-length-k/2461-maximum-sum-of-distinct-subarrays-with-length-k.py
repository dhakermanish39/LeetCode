class Solution(object):
    def maximumSubarraySum(self, nums, k):
        s=0
        temp=sum(nums[:k])
        mp={}
        for i in range(k):
            mp[nums[i]]=mp.get(nums[i],0)+1
        if len(mp)==k:
            s=temp
        for i in range(k,len(nums)):
            temp=temp-nums[i-k]+nums[i]
            mp[nums[i-k]]-=1
            if mp[nums[i-k]]==0:
                del mp[nums[i-k]]
            mp[nums[i]]=mp.get(nums[i],0)+1
            if len(mp)==k:
                s=max(s,temp)
        return s