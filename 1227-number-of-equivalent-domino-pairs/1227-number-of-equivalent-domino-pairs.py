class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        ans = 0
        dc = {}
        for i in range(n):
            a, b = dominoes[i]
            p = (a, b) if a<b else (b, a)
            if p not in dc:
                dc[p] = 0
            ans += dc[p]
            dc[p] +=1
        return ans