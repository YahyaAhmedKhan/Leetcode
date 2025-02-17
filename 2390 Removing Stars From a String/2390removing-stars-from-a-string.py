class Solution:
    def removeStars(self, s: str) -> str:
        l = []
        for c in s:
            if (c == '*'):
                l.pop()
            else: l.append(c)
        return ''.join(l)
        