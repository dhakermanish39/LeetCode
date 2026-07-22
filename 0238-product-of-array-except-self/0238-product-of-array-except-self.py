class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        multi=1
        c=0
        for i in nums:
            if i!=0:

                multi=multi*i
            else:
                c=c+1


        out=[]
        for i in nums:
            if c >1:
                out.append(0)  
            elif c ==1:
                if i==0:
                    out.append(multi)
                else:
                    out.append(0)
            else:
                out.append(multi//i)            


        return out    
        