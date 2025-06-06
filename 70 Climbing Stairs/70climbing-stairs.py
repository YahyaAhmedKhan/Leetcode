class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        ans = [0 for i in range(n+1)]
        ans[1] = 1
        ans[2] = 2
        for i in range(3, n+1):
            ans[i] = ans[i-1] + ans[i-2]
        return ans[n]