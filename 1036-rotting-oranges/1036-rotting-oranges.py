class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        for i in grid:
            print(i)

        fresh = 0
        dq = deque()
        m, n = len(grid), len(grid[0])


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh +=1 
                elif grid[i][j] ==2:
                    dq.appendleft((i, j, 0))
        if fresh == 0: return 0
        
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]

        def isValid(x, y):
            return (x>-1 and x<m and y>-1 and y<n and grid[x][y] == 1)
        while dq:
            x, y, t = dq.pop()

            for x_, y_ in zip(dx, dy):
                newx, newy = x+x_, y+y_
                if isValid(newx, newy):
                    grid[newx][newy] = 2
                    dq.appendleft((newx, newy, t+1))
                    fresh-=1
                    if fresh == 0:
                        return t+1
        return -1

        