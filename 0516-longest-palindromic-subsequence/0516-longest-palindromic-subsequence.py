class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
            if i<n-1:
                dp[i][i+1] = 2 if s[i] == s[i+1] else 1
        
        def helper(l, r):
            if dp[l][r] != -1:
                return dp[l][r]

            if s[l]==s[r]:
                dp[l][r] = helper(l+1, r-1)+2
            else:
                dp[l][r] = max(helper(l, r-1), helper(l+1, r))

            return dp[l][r]

        return helper(0,n-1)
            

        