class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[0]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
            if i<n-1:
                dp[i][i+1] = 2 if s[i]==s[i+1] else 0

        for l in range(3, n+1):
            for i in range(n-l+1):
                left, right = i, i+l-1
                dp[left][right] = dp[left+1][right-1] + 2 if (s[left]==s[right] and dp[left+1][right-1]>0)  else 0


        l, r = 0, 0
        maxi = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j] > maxi:
                    maxi = dp[i][j]
                    l, r = i, j
        return s[l:r+1]


        