from math import inf
class Solution:
    def coinChange(self, coins, amount):           
        #@lru_cache(None)
        def coinChangeInner(rem, cache):
            if rem < 0:
                return inf
            if rem == 0:                    
                return 0       
            if rem in cache:
                return cache[rem]
            #recurrence relation
            cache[rem] = min(coinChangeInner(rem-x, cache) + 1 for x in coins)                         
            return cache[rem]      
        
        ans = coinChangeInner(amount, {})
        return -1 if ans == inf else ans    



if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1,2,5], 11))