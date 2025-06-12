class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vows = set(['a', 'e', 'i', 'o', 'u'])

        curr = 0
        for i in range(k):
            curr+= 1 if s[i] in vows else 0
        ans = curr
        for i in range(k, len(s)):
            curr += 1 if s[i] in vows else 0
            curr -= 1 if s[i-k] in vows else 0
            ans = max(ans, curr)

        return ans
        