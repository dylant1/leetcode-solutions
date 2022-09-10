class Solution:
    def climbStairs(self, n):

        def dp(n, memo):
            if n == 1 or n == 2:
                return n
            if n not in memo:
                memo[n] = dp(n - 2, memo) + dp(n - 1, memo)
            return memo[n]
        return dp(n, {})


# n = 3
# work backwards
# can either go to n = n - 1 or n = n - 2
# now n is either 1 or 2
# we can now go to either n = n - 1 or n = n - 1
# n == 1 is a base case
# n == 0 is also a base case

if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(4))
