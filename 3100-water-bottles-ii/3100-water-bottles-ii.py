class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        res=numBottles
        while numBottles>=numExchange:
            numBottles=numBottles-numExchange
            numExchange+=1
            res+=1
            numBottles+=1
        return res
        