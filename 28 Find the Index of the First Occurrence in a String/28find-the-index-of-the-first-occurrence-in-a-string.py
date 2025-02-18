class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        h = len(haystack)
        for i in range(h-l+1):
            c = 0
            print(c)
            while (haystack[i+c] == needle[c]):
                c+=1
                if (c == l): return i
        return -1


        