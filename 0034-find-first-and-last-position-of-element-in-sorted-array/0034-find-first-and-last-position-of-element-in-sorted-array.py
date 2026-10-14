class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[-1,-1]
        s=0
        e=len(nums)-1
        while s <=e:
            m=(s+e)//2
            if nums[m]==target:
                """res[0],res[1]=m,m
                x=m
                while nums[x]==target:
                    res[0]=x
                    x-=1
                x=m    
                while  nums[x]==target:
                    res[1]=x
                    x+=1
                return res    """   
                if m<res[0] or res[0]==-1:
                    res[0]=m
                e=m-1
            elif nums[m]<target:
                s=m+1
            else:
                e=m-1
        s=0
        e=len(nums)-1
        while s <=e:
            m=(s+e)//2
            if nums[m]==target:
                """res[0],res[1]=m,m
                x=m
                while nums[x]==target:
                    res[0]=x
                    x-=1
                x=m    
                while  nums[x]==target:
                    res[1]=x
                    x+=1
                return res    """   
                if m>res[1]:
                    res[1]=m
                s=m+1
            elif nums[m]<target:
                s=m+1
            else:
                e=m-1        

        return res                
        