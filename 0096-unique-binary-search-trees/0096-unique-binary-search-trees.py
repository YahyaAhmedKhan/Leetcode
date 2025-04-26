class Solution:
    def numTrees(self, n: int) -> int:

        dp = [None]*(n+1)

        def helper(k):

            if k<=1:
                return 1
            if dp[k] is not None:
                return dp[k]
            ans = 0
            for i in range(1, k+1):
                ans += helper(i-1)*helper(k-i)
            dp[k] = ans
            return dp[k]
        return helper(n)
        