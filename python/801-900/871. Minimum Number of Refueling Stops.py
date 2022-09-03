class Solution:
    def minRefuelStops(self, target, startFuel, stations) -> int:
        self.stations = stations
        self.startFuel = startFuel
        for k in range(len(stations)+1):
            if self.dp(k,len(stations)-1) >= target:
                return k
        return -1
    
    import functools
    @functools.lru_cache(10**6)
    def dp(self,k,i):
        if i==-1:
            return self.startFuel 
        if k==0:
            return self.startFuel
        return max(self.dp(k-1,i-1)+self.stations[i][1] if self.dp(k-1,i-1)>=self.stations[i][0] else 0, self.dp(k,i-1))


#THIS IS A VARIATINO OF KNAPSACK
#NO CLUE HOW TO SOLVE THOUGH