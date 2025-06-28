class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        lens = [float("inf")]*(n+1)
        lens[0] = 0

        def find(i):
            nonlocal n
            l, r = 0, n
            ans = 0
            while l<=r:
                mid = (l+r)//2

                if lens[mid]<=i:
                    ans = mid
                    l = mid+1
                else:
                    r = mid-1
            return ans
        ret = [0]*n

        for i in range(n):
            val = obstacles[i]
            maxlen = find(val)
            # print(lens)
            # print(val, maxlen)
            lens[maxlen+1] = min(val, lens[maxlen+1])

            ret[i] = maxlen+1
        return ret




                    
        