class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [None] * len(s)

        def helper(i):
            if i==len(s):
                return 1
            
            if dp[i] is not None:
                return dp[i]

            if s[i] == "0":
                dp[i] = 0
            elif i<len(s)-1 and (int(s[i]+s[i+1])<27) :
                dp[i] = helper(i+1) + helper(i+2)
            else:
                dp[i] = helper(i+1)

            return dp[i]
        ans = helper(0)
        print(dp)
        return ans


            


        