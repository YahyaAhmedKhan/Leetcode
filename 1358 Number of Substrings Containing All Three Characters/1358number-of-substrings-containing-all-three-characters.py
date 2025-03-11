class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, r = 0, 0
        dc = {'a':0, 'b':0, 'c':0}

        def isval():
            for i in dc.values():
                if i == 0: return False
            return True

        ans = 0
        r = -1
        while l<len(s)-2:
            while not isval():
                if r<len(s)-1:
                    r+=1
                    dc[s[r]]+=1
                else: return ans
            
            ans += len(s)-r
            dc[s[l]]-=1
            l+=1
        return ans

            