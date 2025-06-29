class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [None]*len(questions)
        def helper(i):
            if i >= len(questions):return 0
            if dp[i] is not None:
                return dp[i]
            pwr, cst = questions[i][0], questions[i][1]
            dp[i] = max(helper(i+cst+1)+pwr, helper(i+1))
            return dp[i]

        return helper(0)

        