# import pdb

class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        def backtrack(S = [], openP = 0, closedP = 0):
            # if number of pairs, base case
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            # if open parentheses is less than the number of pairs, we know that we can add more
            if openP < n:
                #add
                S.append("(")
                #backtrack
                backtrack(S, openP+1, closedP)
                #remove
                S.pop()
            # we must make sure that there are open parentheses availible to be closed
            if closedP < openP:
                #add
                S.append(")")
                #backtrack
                backtrack(S, openP, closedP+1)
                #remove
                S.pop()
        backtrack()
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(6))
    