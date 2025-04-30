class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        n = len(nums)
        r = 0
        curr_maxis = 0
        ans = 0
        for l in range(n):

            while (r<len(nums) and curr_maxis<k):
                if nums[r]==maxi: curr_maxis+=1
                r+=1
            if curr_maxis==k:
                print(l, r)
                ans += n-r+1

            if nums[l] == maxi:
                curr_maxis-=1

        return ans



            
        