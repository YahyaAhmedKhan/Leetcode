class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        h = height
        l, r = 0, n-1
        ans = -1
        while l<r:
            w = r-l
            ans = max(ans, w*min(h[l], h[r]))
            print(ans, l, r)
            if h[l]<h[r]:
                l+=1
            else: r-=1

        return ans
        