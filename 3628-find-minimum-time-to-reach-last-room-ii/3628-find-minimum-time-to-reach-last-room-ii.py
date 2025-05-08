class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        
        dist = [ [ [float("inf")]*2 for i in range(m) ] for j in range(n) ]

        # dist[0][0] = (0, float("inf"))

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        def isValid(i, j):
            nonlocal n, m
            return (i>-1 and i<n and j>-1 and j<m)

        hp = []

        heappush(hp, (0, 0, 0, 0))
        while hp:
            d, i, j, isTwo =  heappop(hp)
            if d >= dist[i][j][isTwo]: continue
            dist[i][j][isTwo] = d
            for x, y in zip(dx, dy):
                newx, newy = i+x, j+y
                if isValid(newx, newy):
                    newd = max(d, moveTime[newx][newy])
                    newd += 2 if isTwo else 1
                    if newd < dist[newx][newy][1-isTwo]:
                        heappush(hp, (newd, newx, newy, 1-isTwo))

        return min(dist[n-1][m-1])