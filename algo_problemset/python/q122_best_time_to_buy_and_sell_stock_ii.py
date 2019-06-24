"""

122. Best Time to Buy and Sell Stock II
Easy
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0

        prev_x, max_profit = prices[-1], 0
        for x in reversed(prices[:-1]):
            if x < prev_x:
                max_profit += prev_x - x
            prev_x = x

        return max_profit
