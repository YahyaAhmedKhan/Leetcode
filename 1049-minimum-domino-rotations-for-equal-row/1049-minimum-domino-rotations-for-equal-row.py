class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        dc = {i:0 for i in range(1, 9)}
        for i in range(n):
            dc[tops[i]] +=1
            dc[bottoms[i]] +=1
            if tops[i] == bottoms[i]:
                dc[bottoms[i]] -=1
        
        ans = float("inf")
        for k in list(dc.keys()):
            if dc[k] == n:
                c = tops.count(k)
                ans = min(ans, min(c, n-c))
                c = bottoms.count(k)
                ans = min(ans, min(c, n-c))


        return -1 if isinf(ans) else ans


            
