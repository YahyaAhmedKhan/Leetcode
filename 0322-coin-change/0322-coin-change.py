class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)

        if coins[0]<=amount:
            dp[coins[0]] = 1
        dp[0] = 0

        for i in range(len(coins)):
            for t in range(amount+1):
                if coins[i]<= t:
                    dp[t] = min(dp[t], dp[t-coins[i]]+1)

        return dp[amount] if not isinf(dp[amount]) else -1

        