class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        dp = [[[None, None, None] for _ in range(2)] for i in range(n) ]

        for i in range(3):
            dp[0][0][i] = 0
            dp[0][1][i] = -prices[0]
        

        def helper(i, bought, rem):

            if dp[i][bought][rem] is not None:
                return dp[i][bought][rem]
            
            if bought:
                dp[i][bought][rem] = max(helper(i-1, 0, rem)-prices[i], helper(i-1, 1, rem))

            else:
                if rem==2:
                    dp[i][bought][rem] = helper(i-1, 0, rem)
                else:
                    dp[i][bought][rem] = max(helper(i-1, 1, rem+1)+prices[i], helper(i-1, 0, rem))
            
            return dp[i][bought][rem]

        return max(helper(n-1, 0, 0), helper(n-1, 0, 1), helper(n-1, 0, 2))

        



        