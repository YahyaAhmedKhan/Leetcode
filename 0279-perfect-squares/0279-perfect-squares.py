class Solution:
    def numSquares(self, n: int) -> int:
        
        if n==1: return 1
        
        k = 1
        while k*k<=n:
            k+=1
        k-=1
        dp = [[0]*(n+1) for i in range(k)]
        
        dp[0][0] = float("inf")
        for i in range(k):
            dp[i][0] = 0
        
        for i in range(n+1):
            dp[0][i] = i

        for i in range(1, k):
            for j in range(1, n+1):
                v = i+1
                if v*v <=j:
                    dp[i][j] = min(dp[i][j-v*v]+1, dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[k-1][n]




        