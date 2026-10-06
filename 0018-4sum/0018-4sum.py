class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                s=j+1
                e=len(nums)-1
                while s<e:
                    if nums[i]+nums[j]+nums[s]+nums[e] == target:
                        if sorted([nums[i],nums[j],nums[s],nums[e]]) not in res:
                            res.append(sorted([nums[i],nums[j],nums[s],nums[e]]))
                        s+=1    
                            
                    elif nums[i]+nums[j]+nums[s]+nums[e] < target :
                        s+=1
                    else :
                        e-=1
        return res                          

        