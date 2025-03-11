class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        dc = {}
        vows = ['a', 'e', 'i', 'o', 'u']
        vows = set(vows)
        for i in vows:
            dc[i] = 0

        def isvows():
            for i in vows:
                if dc[i] == 0: return False
            return True

        cons=0
        def addc(c):
            nonlocal cons
            if c in vows:
                dc[c]+=1
            else:
                cons+=1
        def removec(c):
            nonlocal cons
            if c in vows:
                dc[c]-=1
            else:
                cons-=1

        def helper(kk):
            nonlocal cons
            ans = 0
            cons = 0
            l, r = 0, -1
            for i in vows:
                dc[i] = 0
            while l<len(word):
                while not isvows() or cons<kk:
                    # print (l, r)
                    # print(word[l:r+1])
                    # print(dc, cons)
                    if r<len(word)-1:
                        r+=1
                        addc(word[r])
                    else: return ans
                ans += len(word)-r
                removec(word[l])
                l+=1
            return ans
        a, b = helper(k),helper(k+1)
        print(a, b)
        return a-b