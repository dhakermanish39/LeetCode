class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        return abs(int(str(n)[::-1]) - n)
        