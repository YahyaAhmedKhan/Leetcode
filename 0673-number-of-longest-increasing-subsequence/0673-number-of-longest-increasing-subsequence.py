class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(1, 1) ]*n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[j][0]+1 > dp[i][0]:
                        dp[i] = (dp[j][0]+1, dp[j][1])
                    elif dp[j][0]+1 == dp[i][0]:
                        dp[i] = (dp[i][0], dp[i][1]+dp[j][1])

        m = -1
        for x, y in dp:
            m = max(m, x)
        ans = 0
        for x, y in dp:
            if x==m:
                ans+=y

        print(dp)

        return ans

        