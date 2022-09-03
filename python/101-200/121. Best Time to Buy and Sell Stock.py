class Solution:
    def maxProfit(self, prices):
        start = 0
        res = 0
        for end in range(len(prices)):
            if prices[end] > prices[start]:
                res = max(res, prices[end] - prices[start])
            else:
                start = end
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))