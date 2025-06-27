class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0]*(i+1) for i in range(len(triangle))]
        depth = len(triangle)


        for i in range(len(dp[-1])):
            dp[-1][i] = triangle[-1][i]

        for d in range(depth-2, -1, -1):
            for i in range(len(dp[d])):
                dp[d][i] = min(dp[d+1][i], dp[d+1][i+1])+triangle[d][i]

        return dp[0][0]