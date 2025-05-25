class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dc = {}

        n = len(words)
        ans = 0
        for i in range(n):
            a, b = tuple(words[i])
            forw, back = a+b, b+a
            if dc.get(back, 0) == 0:
                dc[forw] = dc.get(forw, 0)+1
            else:
                dc[back] -= 1
                ans+=4
        
        for i in list(dc.keys()):
            if i[0] == i[1] and dc[i]>0:
                return ans+2

        return ans

            
            