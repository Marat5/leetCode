from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = float("inf")
        bestProfit = 0
        for p in prices:
            profit = p - buyPrice
            bestProfit = max(bestProfit, profit)
            buyPrice = min(p, buyPrice)

        return bestProfit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
