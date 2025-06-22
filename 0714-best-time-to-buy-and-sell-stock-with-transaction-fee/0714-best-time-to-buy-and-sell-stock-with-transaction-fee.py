class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        dp = [[None, None] for i in range(len(prices))]
        n = len(prices)

        dp[0][1] = -1*prices[0]
        dp[0][0] = 0
        def helper(i, bought):
            nonlocal fee
            if dp[i][bought]!=None:
                return dp[i][bought]

            if not bought:
                ans = max(helper(i-1, 0), helper(i-1, 1)+prices[i]-fee)
                dp[i][bought] = ans

            else:
                ans = max(helper(i-1, 0)-prices[i], helper(i-1, 1))
                dp[i][bought] = ans


            return dp[i][bought]


        ans = helper(n-1, 0)
        return ans

            


        