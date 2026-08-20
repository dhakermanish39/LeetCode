class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]

        for num in nums:
           new_subsets = []

           for subset in result:
               new_subsets.append(subset + [num])

           result += new_subsets

        return result