class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        maxs = [0]*len(nums)
        maxi = nums[-1]
        for i in range(len(nums)-1, 1, -1):
            maxi  = max(maxi, nums[i])
            maxs[i] = maxi

        highs = [0]*len(nums)
        lows = [0]*len(nums)

        a, b = nums[0], nums[0]

        for i in range(len(nums)):
            a = max(a, nums[i])
            b = min(b, nums[i])
            highs[i] = a
            lows[i] = b
    
        ans = 0
        for k in range(2, len(nums)):
            ans = max((highs[k-2]-nums[k-1]) * maxs[k], ans)

        return ans

    