class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def doesDivide(s1, s2):
            n, m = len(s1), len(s2)
            ans = ""
            for i in range(n//m):
                ans+=s2
            print(s1, s2, s1==ans)
            return s1==ans

        n, m = len(str1), len(str2)
        if n==0 or m==0:
            return ""
        ans = ""
        for i in range(0, (min(n, m))):
            div = str1[:i+1]
            d = len(div)
            if not (n%d + m%d):
                if doesDivide(str1, div) and doesDivide(str2, div):
                    ans = div
        return ans

        