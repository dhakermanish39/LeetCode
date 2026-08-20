class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        x =[]
        y =[]

        for i in nums1:
            if i not in nums2:
                x.append(i)
        
        for j in nums2:
            if j not in nums1:
                y.append(j)

        return [list(set(x)),list(set(y))]

        