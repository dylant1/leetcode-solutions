import heapq
from collections import defaultdict
class Solution:
    #DONT UNDERSTAND THIS SOLUTION, COME BACK TO THIS
    def isPossible(self, L):
        tails = defaultdict(list)

        for n in L:
            if tails[n - 1]:
                heapq.heappush(tails[n], heapq.heappop(tails[n - 1]) + 1)
            else:
                heapq.heappush(tails[n], 1)

        return all(
            l >= 3
            for tail in tails.values()
            for l in tail
        )