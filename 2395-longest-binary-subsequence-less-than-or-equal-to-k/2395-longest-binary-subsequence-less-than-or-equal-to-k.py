class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        total = 0
        l = 0
        for c in reversed(s):
            val = 1 if c=="1" else 0
            if not val:
                l+=1
            else:
                newval = total+(1<<l)
                if newval<=k:
                    l+=1
                    total=newval

        return l
                

