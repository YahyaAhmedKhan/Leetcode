class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        maxi = max(candies)

        l, r = 1, maxi
        mid = (l+r)//2

        def check(c):
            ans = 0
            for i in candies:
                ans += i//c
                if ans >= k:
                    return True
            return ans>=k
        ans = 0
        while l<=r:
            mid = (l+r)//2
            # if mid 
            if check(mid):
                ans = mid
                l=mid+1
            else:
                r=mid-1
        
        return ans


        