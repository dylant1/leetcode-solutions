class Solution:
    def rotate(self, matrix):
        #transpose
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        #reverse
        for row in matrix:
            row = row.reverse()
        return matrix
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))