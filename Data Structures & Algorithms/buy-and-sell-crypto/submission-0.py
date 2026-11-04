class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0
        for v in prices:
            profit = v - lowest
            if profit > max_profit:
                max_profit = profit
            if v < lowest:
                lowest = v
        return max_profit