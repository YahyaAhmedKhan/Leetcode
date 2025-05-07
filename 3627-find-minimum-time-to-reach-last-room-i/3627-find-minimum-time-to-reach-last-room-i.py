class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n  = len(moveTime[0]), len(moveTime)

        curr = (0, 0, 0) # d, i, j

        hp = []
        heappush(hp, curr)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def isValid(i, j):
            nonlocal n, m
            ans =  (i<n and i>-1 and j<m and j>-1)
            return ans

        dist = [[float("inf")]*m for _ in range(n)]
        while hp:
            d, i, j = heappop(hp)

            if d >= dist[i][j]: continue
            dist[i][j] = d

            for x, y in zip(dx, dy):
                if isValid(i+x, j+y):
                    newx, newy = i+x, j+y
                    newd = max(d, moveTime[newx][newy])+1

                    if newd < dist[newx][newy]:
                        heappush(hp, (newd, newx, newy))

        return dist[n-1][m-1]
                    




        