class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        dp = [[None, None] for i in range(len(prices))]
        n = len(prices)
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        def helper(i, bought):
            if dp[i][bought] is not None:
                return dp[i][bought]

            if bought:
                dp[i][bought] = max(helper(i-1, 0)-prices[i], helper(i-1, 1))
            else:
                dp[i][bought] = max(helper(i-1, 1)+prices[i]-fee, helper(i-1, 0))

            return dp[i][bought]


        ans =  helper(n-1, 0)
        print(dp)
        return ans

            


        