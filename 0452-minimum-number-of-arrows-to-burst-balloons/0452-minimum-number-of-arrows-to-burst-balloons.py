class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        tups = sorted(list(map(tuple, points)))
        ans = 0
        leftmostend = float("-inf")
        print(tups)
        for i, t in enumerate(tups):
            s, e = t
            if s<=leftmostend:
                leftmostend = min(leftmostend, e)
            else:
                leftmostend = e
                ans+=1

        return ans
        