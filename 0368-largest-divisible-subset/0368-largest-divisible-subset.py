class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        nums.sort()
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)

        print(dp)
        ret = []

        maxi = dp.index(max(dp))
        print(maxi)
        ret.append(nums[maxi])
        maxx = dp[maxi]-1


        for i in range(maxi, -1, -1):
            if dp[i] == maxx and (ret[-1]%nums[i]==0):
                maxx-=1
                ret.append(nums[i])

        return ret







        
        