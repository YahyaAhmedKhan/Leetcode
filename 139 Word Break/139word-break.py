class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s) 
        dp = [False for i in range(l+1)]
        dp[0] = True

        for i in range(l+1):
            for j in range(i):
                if (dp[j] and (s[j:i] in wordDict)):
                    dp[i] = True

        return dp[l]        