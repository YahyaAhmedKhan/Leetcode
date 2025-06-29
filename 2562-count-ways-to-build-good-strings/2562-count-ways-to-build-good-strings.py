class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        dp = [None]*(high+1)
        dp[0] = 1

        def helper(i):
            nonlocal zero, one
            if dp[i] is not None: return dp[i]
            z = 0 if zero > i else helper(i-zero)
            o = 0 if one > i else helper(i-one)

            dp[i] = (z+o)%(1e9+7)
            return dp[i]

        ans = 0
        for i in range(low, high+1):
            ans += helper(i)
            ans %= (1e9+7)
        return int(ans)


        
        