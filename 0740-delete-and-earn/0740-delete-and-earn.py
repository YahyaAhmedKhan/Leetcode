class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        freq=[0]*(max(nums)+1)
        for c in nums:
            freq[c]+=1

        n = max(nums)
        dp = [0]*(n+1)

        dp[1]=freq[1]

        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+freq[i]*i)
        return dp[n]


        

        # def helper(i):
        #     if i==0:
        #         return arr[i]*dc[arr[i]]
        #     if i==1:
        #         return max(arr[i]*dc[arr[i]], arr[i-1]*dc[arr[i-1]])

        #     if dp[i]!=-1: return dp[i]

        #     dp[i] = max(helper(i-2)+dc[arr[i]]*arr[i], helper(i-1))
        #     return dp[i]

        # return helper(n-1)

            