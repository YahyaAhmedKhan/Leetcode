class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
    
        n, m = len(maze), len(maze[0])
        visit = [[0]*m for i in range(n)]

        for i in maze:
            print(i)

        def isvalid(x, y):
            if (-1<x<n) and (-1<y<m):

                if maze[x][y]=="." and not visit[x][y]:
                    return True

            return False

        dq = deque()
        start = tuple(entrance)
        dq.append((start, 0))
        visit[entrance[0]][entrance[1]] = 1

        while dq:
            cell, d = dq.popleft()
            i,j = cell
            for x, y in zip(dx, dy):
                newx, newy = i+x, j+y

                if isvalid(newx, newy):
                    visit[newx][newy] = 1
                    if (newx in (0, n-1)) or newy in (0, m-1):
                        return d+1
                    dq.append(((newx, newy), d+1))

        return -1





    
