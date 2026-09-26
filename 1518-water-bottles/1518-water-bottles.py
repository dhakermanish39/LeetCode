class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        res=numBottles
        while numBottles>0:
            res=res+numBottles//numExchange
            if (numBottles//numExchange)+(numBottles%numExchange)>=numExchange:
                numBottles=(numBottles//numExchange)+(numBottles%numExchange)
            else:numBottles=(numBottles//numExchange)

        return res    
        