class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        C = amount
        n = len(coins)
        dp = [[0 for i in range(C+1)] for i in range(n+1)]
        for i in range (1, C+1):
            dp[0][i] = float('inf')


        for i in range(1, n+1):
            for j in range(1, C+1):
                if (j - coins[i-1] > -1):
                    dp[i][j] = min(dp[i][j - coins[i-1]] + 1, dp[i-1][j], dp[i-1][j - coins[i-1]] + 1)
                else:
                    dp[i][j] = dp[i-1][j]
        if dp[n][C] == float('inf'):
            return -1
        return dp[n][C]
        
        