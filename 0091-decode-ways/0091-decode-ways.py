class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s)+1)
        n = len(s)
        dp[n-1] = 0 if s[n-1]=="0" else 1

        for i in range(n-2, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            elif int(s[i:i+2]) < 27:

                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]


        return dp[0]


        