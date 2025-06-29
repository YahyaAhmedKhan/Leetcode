class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        tups = list(map(tuple, envelopes))
        tups= sorted(tups, key = lambda x: (x[0], -x[1]))
        print(tups)
        n = len(envelopes)
        lens = [float("inf") for _ in range(n+1)]
        lens[0] = 0
        def find(val):
            nonlocal n
            l, r = 0, n

            ans = 0
            while l<=r:
                mid = (l+r)//2
                if lens[mid]<val:
                    ans = mid
                    l= mid+1
                else:
                    r = mid-1
            return ans
            
        ret = -1
        for i in range(n):
            h = tups[i][1]

            minh = find(h)
            ret = max(ret, minh+1)

            lens[minh+1] = min(lens[minh+1], h)


        return ret
