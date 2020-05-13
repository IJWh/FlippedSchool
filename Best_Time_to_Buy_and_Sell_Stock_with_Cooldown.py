# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/submissions/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = [-float(inf),-float(inf)]
        held = [-float(inf),-float(inf)]
        reset = [0,0]
        max_profit = 0
        
        for i in range(0, len(prices)):
            sold[i%2] = held[(i-1)%2] + prices[i]
            held[i%2] = max(held[(i-1)%2], reset[(i-1)%2] - prices[i])
            reset[i%2] = max(reset[(i-1)%2],sold[(i-1)%2])
            
            
            
        max_profit = max(max_profit,sold[(len(prices)-1)%2])
        max_profit = max(max_profit,held[((len(prices)-1)%2)])
        max_profit = max(max_profit,reset[((len(prices)-1)%2)])
        
            
        return max_profit
            
        
        
