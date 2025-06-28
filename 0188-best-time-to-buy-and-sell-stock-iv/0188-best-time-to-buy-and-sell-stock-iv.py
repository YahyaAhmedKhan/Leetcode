class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[None]*(k+1) for _ in range(2)] for i in range(n) ]

        for i in range(k+1):
            dp[0][0][i] = 0
            dp[0][1][i] = -prices[0]
        

        def helper(i, bought, rem):
            print(i, bought, rem)
            if dp[i][bought][rem] is not None:
                return dp[i][bought][rem]
            
            if bought:
                dp[i][bought][rem] = max(helper(i-1, 0, rem)-prices[i], helper(i-1, 1, rem))
            else:
                if rem==k:
                    dp[i][bought][rem] = helper(i-1, 0, rem)
                else:
                    dp[i][bought][rem] = max(helper(i-1, 1, rem+1)+prices[i], helper(i-1, 0, rem))
            
            return dp[i][bought][rem]

        maxi = 0
        for i in range(k+1):
            maxi = max(helper(n-1, 0, i), maxi)

        return maxi
