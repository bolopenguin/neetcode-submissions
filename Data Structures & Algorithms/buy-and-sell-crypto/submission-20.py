class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1

        max_profit = 0
        for idx, price_buy in enumerate(prices):
            for price_sell in prices[(idx + 1):]:
                max_profit = max(max_profit, price_sell - price_buy)

        return max_profit