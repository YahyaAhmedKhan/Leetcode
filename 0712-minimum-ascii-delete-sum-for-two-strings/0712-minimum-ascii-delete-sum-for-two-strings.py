class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        a, b = 0, 0
        for c in s1:
            a+=ord(c)
        for c in s2:
            b+=ord(c)

        m, n = len(s1), len(s2)
        dp = [[None]*(n+1)  for i in range(m+1)]

        dp[0][0] = 0
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0]+ord(s1[i-1])
        for i in range(1, n+1):
            dp[0][i] = dp[0][i-1] + ord(s2[i-1])

        print(dp)

        for i in range(1, m+1):
            for j in range(1, n+1):

                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] =  min( dp[i-1][j] + ord(s1[i-1]) , dp[i][j-1] + ord(s2[j-1]) )

        return dp[m][n]
            
        