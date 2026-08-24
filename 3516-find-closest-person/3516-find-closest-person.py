class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        return 1 if abs(z-x) < abs(z-y) else 2 if abs(z-x) > abs(z-y) else 0
        