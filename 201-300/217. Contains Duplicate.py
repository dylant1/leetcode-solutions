class Solution:
    def containsDuplicate(self, nums) -> bool:
        seen = {}
        
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen[nums[i]] = 1
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([3, 2, 4, 6, 8, 4]))
    print(sol.containsDuplicate([1, 2, 3, 4, 5, 6]))