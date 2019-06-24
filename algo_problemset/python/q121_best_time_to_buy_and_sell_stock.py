"""

121. Best Time to Buy and Sell Stock
Easy
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0

        sell_price, max_profit = 0, 0
        for price in reversed(prices):
            if price > sell_price:
                sell_price = price
            max_profit = max(max_profit, sell_price-price)
        return max_profit
