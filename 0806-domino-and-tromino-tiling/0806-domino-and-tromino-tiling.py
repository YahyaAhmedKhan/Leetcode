class Solution:
    def numTilings(self, n: int) -> int:

        dp = [[-1]*2 for _ in range(n+1)]

        dp[0][0]= 1
        dp[0][1]= 0
        dp[1][0]= 2
        dp[1][1]= 1

        def helper(i, state):

            if dp[i][state]!=-1:
                return dp[i][state]

            if state == 0:
                ans = 2*helper(i-1, 1) + helper(i-1, 0) + helper(i-2, 0)
                dp[i][state] = ans %(1e9+7)
                return int(dp[i][state])
            else:
                ans = helper(i-2, 0) + helper(i-1, 1)
                dp[i][state] = ans % (1e9+7)
                return int(dp[i][state])

        return helper(n-1, 0)


        