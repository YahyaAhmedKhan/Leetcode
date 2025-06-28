class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1: return 0
        n = len(prices)
        dp = [[None, None] for _ in range(n)]   
        dp[0][1] = -prices[0]
        dp[0][0] = 0
        dp[1][0] = max(prices[1]-prices[0], 0)
        dp[1][1] = max(-prices[0], -prices[1])

        def helper(i, bought):
            if dp[i][bought] is not None:
                return dp[i][bought]

            if bought:
                dp[i][1] = max(helper(i-2, 0)-prices[i], helper(i-1, 1))

            else:
                dp[i][0] = max(helper(i-1, 1)+prices[i], helper(i-1, 0))

            return dp[i][bought]


        ans = helper(n-1, 0)
        return ans
            
