class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s_s=0
        s_d=0
        s_o=0
        for i in nums:
            if i in range(0,10):
                s_s+=i
            elif i in range(10,100):
                s_d+=i 
            else :
                s_o+=i
        return  s_s> s_d+s_o or s_d > s_s+s_o              
        