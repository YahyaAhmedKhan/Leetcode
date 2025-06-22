class Solution:
    def numTilings(self, n: int) -> int:

        dp = [[-1, -1] for i in range(n)]

        dp[0][0] = 1
        dp[0][1] = 0
        if n==1:
            return 1
        dp[1][0] = 2
        dp[1][1] = 2

        def helper(i, spacesLeft):
            if dp[i][spacesLeft]!=-1:
                return dp[i][spacesLeft]

            if spacesLeft==0:
                dp[i][spacesLeft] = helper(i-1, 0) + helper(i-1, 1) + helper(i-2, 0)
                dp[i][spacesLeft]%=(1e9+7)
            else:
                dp[i][spacesLeft] = helper(i-1, 1) + 2*helper(i-2, 0)
                dp[i][spacesLeft]%=(1e9+7)
            return dp[i][spacesLeft]

        ret = int(helper(n-1, 0))

        return ret
        