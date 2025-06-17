class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        comps = 0
        n = len(isConnected)
        visit = [0]*n
        def dfs(u):
            visit[u] = 1
            for v in range(n):
                if isConnected[u][v] and (not visit[v]):
                    dfs(v)

        for i in range(n):
            if not visit[i]:
                dfs(i)

                comps+=1


        return comps

        