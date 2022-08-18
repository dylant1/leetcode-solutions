class Solution:
    def twoSum(self, nums, target):
        m = {}
        
        for i in range(len(nums)):
            if target - nums[i] in m:
                return [i, m[target - nums[i]]]
            m[nums[i]] = i
        return -1
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([3, 5, 7, 1, 2], 10))