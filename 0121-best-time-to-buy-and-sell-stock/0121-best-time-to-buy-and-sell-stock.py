class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0
        for i in prices:
            min_price=min(min_price,i)
            max_profit=max(max_profit,i-min_price)
            
        return max_profit