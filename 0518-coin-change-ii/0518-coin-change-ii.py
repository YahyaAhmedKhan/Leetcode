class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n, m = amount, len(coins)

        dp = [[0]*(n+1) for i in range(m)]

        for i in range(n+1):
            dp[0][i] = 0 if i%coins[0] else 1

        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n+1):
                
                if coins[i]<=j:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

                else:
                    dp[i][j] = dp[i-1][j]

        return dp[m-1][amount]
        