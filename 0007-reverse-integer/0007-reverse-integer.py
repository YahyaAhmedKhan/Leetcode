class Solution:
    def reverse(self, x: int) -> int:
        # lim = 2**31-1
        # print(lim)
        lim = 2147483647

        ans = 0
        t = abs(x)
        while t>0:
            dig = t%10
            ans+=dig
            ans*=10
            t//=10
        
        ans//=10
        if x<0:
            ans *= -1

        if abs(ans)> lim:return 0
        else: return ans

        