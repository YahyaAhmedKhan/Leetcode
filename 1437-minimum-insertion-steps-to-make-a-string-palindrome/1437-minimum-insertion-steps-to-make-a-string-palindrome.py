class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[None]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 0
            if i<n-1:
                dp[i][i+1] = 0 if s[i]==s[i+1] else 1

        def helper(i, j):
            if dp[i][j] is not None:
                return dp[i][j]

            if s[i]==s[j]:
                dp[i][j] = helper(i+1, j-1)
            else:
                dp[i][j] = min(helper(i+1, j), helper(i, j-1)) + 1

            return dp[i][j]

        return helper(0, n-1)
        