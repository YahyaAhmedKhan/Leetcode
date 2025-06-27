class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[0]*n for _ in range(m) ]

        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(1, m):
            for j in range(n):
                left = float("inf") if j==0 else dp[i-1][j-1]
                right = float("inf") if j==n-1 else dp[i-1][j+1]

                dp[i][j] = min(left, right, dp[i-1][j]) + matrix[i][j]

        return min(dp[-1])
