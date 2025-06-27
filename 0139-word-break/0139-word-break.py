class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [None]*(n+1)
        dc = set(wordDict)
        dp[0] = True

        def helper(i):
            if dp[i] is not None: return dp[i]

            for start in range(i):
                endword = s[start:i]
                print(endword)
                if endword in dc and helper(start):
                    dp[i] = True
                    return dp[i]
            dp[i] = False
            return dp[i]
        print(dp)
        return helper(n)


        