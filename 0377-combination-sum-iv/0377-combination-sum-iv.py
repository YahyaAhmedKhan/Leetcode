class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        m = len(nums)

        dp = [[0]*(target+1) for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1


        for t in range(1, target+1):
            for i in range(m):
                if nums[i]< t:
                    for k in range(m):
                        dp[i][t]+=dp[k][t-nums[i]]
                elif nums[i]==t:
                    dp[i][t] = 1


        ans =0

        for i in range(m):
            ans+=dp[i][target]
        return ans
                
