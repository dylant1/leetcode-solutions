class Solution:
    def combinationSum2(self, candidates, target):
        # make sure we dont get duplicates, O(nlogn)
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2([1, 2, 3, 4], 5))
    