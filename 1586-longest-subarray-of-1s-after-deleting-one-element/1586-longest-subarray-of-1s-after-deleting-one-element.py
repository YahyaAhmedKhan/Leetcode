class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        ans = 0
        flag = False
        used_flaf = False

        while True:

            while (r<n and (not flag or nums[r]==1)):
                if nums[r] == 0:
                    flag = True
                r+=1

            ans = max(ans, r-l)

            if r==n: return ans-1

            if nums[l]==0:
                flag = False
            l+=1
        