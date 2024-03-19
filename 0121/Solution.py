from typing import List

class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        g = 0
        l = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < l:
                l = prices[i]
            else:
                g = max(g, prices[i] - l)

        return g
    
    def maxProfit2(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxP