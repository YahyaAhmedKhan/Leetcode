class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        col = [-1]*(n+1)
        graph = [[] for _ in range(n+1)]

        for u, v in dislikes: 
            graph[u].append(v)
            graph[v].append(u)
        
        visit = [0]*(n+1)
        def dfs(u, color):
            if visit[u]: return True
            visit[u]=1
            if col[u] == -1:
                col[u] = color
            
            print(u, color)

            for v in graph[u]:
                if not visit[v]:
                    ans = dfs(v, 1-color)
                    if not ans: return False
                else:
                    if color==col[v]:
                        return False
            return True

        for i in range(1, n+1):
            if not dfs(i, 0):
                return False
        return True