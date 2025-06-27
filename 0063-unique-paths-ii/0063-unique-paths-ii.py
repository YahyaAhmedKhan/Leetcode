class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m, n = len(grid), len(grid[0])

        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1 if not grid[0][0] else 0 

        for i in range(1, m):
            dp[i][0] = 0 if (grid[i][0] or not dp[i-1][0]) else 1
        for i in range(1, n):
            dp[0][i] = 0 if (grid[0][i] or not dp[0][i-1]) else 1

            

        
        for i in range(1, m):
            for j in range(1, n):
                if not grid[i][j]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]