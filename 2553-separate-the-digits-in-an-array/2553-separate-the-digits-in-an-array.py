class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums= "".join(map(str,nums))
        nums=list(map(int , nums))
        return nums