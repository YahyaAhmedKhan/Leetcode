class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        m = len(s)
        n = len(t)
        dp = [[None]*(n+1) for _ in range(m+1)]

        


        def helper(i, j):
            if j==0:
                return 1
            if i<j:
                return 0
            if i==j:
                return 1 if s[:i]==t[:j] else 0
            print(i, j)
            if dp[i][j] is not None: return dp[i][j]

            if s[i-1]==t[j-1]:
                dp[i][j] = helper(i-1, j-1)+helper(i-1, j)
            else:
                dp[i][j] = helper(i-1, j)

            return dp[i][j]

        return helper(m, n)
        