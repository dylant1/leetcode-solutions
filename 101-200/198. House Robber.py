class Solution:
    def dfs(self, nums, index, n, dp):
            if index>=n:
                return 0

            if dp[index]!=-1:
                return dp[index]

            including = nums[index]+self.dfs(nums, index+2, n, dp)
            excluding = self.dfs(nums, index+1, n, dp)

            dp[index] = max(including, excluding)
            return dp[index]

    def rob(self, nums):
        dp = [-1]*len(nums)
        return self.dfs(nums, 0, len(nums), dp)
