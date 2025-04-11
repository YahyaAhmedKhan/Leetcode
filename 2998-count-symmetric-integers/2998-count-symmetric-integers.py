class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        def issym(s: str) -> int:
            if len(s)%2==1: return False
            l, r = 0, 0
            for i in range(len(s)//2):
                l+=int(s[i])
            for i in range(len(s)//2, len(s)):
                r+=int(s[i])
            return l==r
        
        ans = 0
        for i in range(low, high+1):
            ans += 1 if issym(str(i)) else 0
        return ans
        