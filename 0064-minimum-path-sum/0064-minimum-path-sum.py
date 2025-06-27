class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        dp = [[-1]*n for i in range(m)]

        for i in range(m):
            dp[i][0] = grid[i][0]+ (0 if i==0 else dp[i-1][0])
          
        for i in range(n):

            dp[0][i] = grid[0][i]+ (0 if i==0 else dp[0][i-1])

        for d in dp: print(d)

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]

        return dp[m-1][n-1]
            


        