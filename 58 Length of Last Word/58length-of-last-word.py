class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = len(s)-1
        while (s[c] == ' '): c -= 1
        ans = 0
        while (c > -1):
            if s[c] != ' ':
                ans += 1
                c -= 1
            else: return ans
        return ans
        