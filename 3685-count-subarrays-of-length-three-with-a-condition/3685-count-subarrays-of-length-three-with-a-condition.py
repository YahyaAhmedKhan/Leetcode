class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        def isValid(i):
            nonlocal n
            if i <= n-3:
                return nums[i+1] == 2*(nums[i] + nums[i+2])
            else: return False

        ans = 0
        for i in range(n):
            ans += 1 if isValid(i) else 0 
        return ans
        