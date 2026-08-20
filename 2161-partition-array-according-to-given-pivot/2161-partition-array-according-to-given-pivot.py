class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        num1=[]
        num2=[]
        num3=[]
        for i in nums:
            num1.append(i) if i<pivot else  num2.append(i) if i> pivot else num3.append(i)
        return num1 +num3+ num2    
        