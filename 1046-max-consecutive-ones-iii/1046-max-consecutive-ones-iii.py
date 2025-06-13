class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, 0
        ans = 0
        currz = k
        while True:
            while (r<n and (nums[r]==1 or currz>0)):
                r+=1
                if nums[r-1]==0:
                    currz-=1
                
            ans = max(ans, r-l)
            if r==n: return ans
            print(l, r)

            l+=1
            if nums[l-1]==0:
                currz+=1
                currz = min(k, currz)

            if r<l:
                r=l

        return ans

        