class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_prices=float('inf')
        max_profit=0
        for price in prices:
            if price<min_prices:
                min_prices=price
            elif (price-min_prices>max_profit):
                max_profit=price-min_prices
        return max_profit
    
hello=Solution()
answer=hello.maxProfit([2,3,4,5,6,7,8,9])
print(answer)
            