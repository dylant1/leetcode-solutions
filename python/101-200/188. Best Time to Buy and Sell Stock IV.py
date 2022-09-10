class Solution:
    def maxProfit(self, k: int, prices):
        
        n = len(prices)
        lookup = {}
        def f(ind, buy, cap, lookup):
            
            if cap == 0: return 0
            
            if ind == n: return 0
            
            if(ind, buy, cap) in lookup: return lookup[(ind, buy, cap)]
            
            profit = 0
            if buy:
                profit = max(f(ind+1, 0, cap, lookup) - prices[ind], f(ind+1, 1, cap, lookup))
            else:
                profit = max(f(ind+1, 1, cap-1, lookup) + prices[ind], f(ind+1, 0, cap, lookup))
                
            lookup[(ind, buy, cap)] = profit
            
            return lookup[(ind, buy, cap)]
        
        return f(0, 1, k, lookup)
        

#NOTE ------- NOT MY SOLUTION
