# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        if not prices:
            return profit
        
        max_p, min_p = prices[-1] , prices[-1]
        
        for p in reversed(prices):
            if max_p < p:
                profit = max(max_p - min_p, profit)
                max_p, min_p = p, p
                
            else:
                min_p = min(min_p, p)
        
        profit = max(max_p - min_p, profit)
        return profit
