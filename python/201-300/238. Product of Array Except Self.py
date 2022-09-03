class Solution:
    def productExceptSelf(self, nums):
        res = [1 for num in nums]

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([2, 3, 4, 1, 0]))
            
