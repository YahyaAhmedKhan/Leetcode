class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]*n
        summ = 0
        for i in range(n):
            summ += nums[i]
            prefix[i] = summ

        print(nums)
        print(prefix)
        
        def getScore(l, r):
            # if l==k: return float("inf")
            s = prefix[r] - (prefix[l-1] if l-1>-1 else 0)
            return (r+1-l)*s
        
        ans = 0
        r = 0
        for l in range(n):
            while r<n and getScore(l, r)<k:
                r+=1
            
            if getScore(l, r-1) < k:
                ans += r-l

        return ans





        