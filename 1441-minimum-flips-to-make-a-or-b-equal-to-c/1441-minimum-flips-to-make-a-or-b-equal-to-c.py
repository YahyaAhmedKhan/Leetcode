class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while c or b or a:
            cc=c%2
            aa, bb = a%2, b%2

            if cc:
                ans += 0 if (aa or bb) else 1
            else:
                ans += (aa+bb)

            print(cc, aa, bb, ans)
            c//=2
            a//=2
            b//=2

        return ans

        