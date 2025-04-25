class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)  
        
        visit = [0]*n

        def dfs(u, e):
            visit[u] = 1
            for v in graph[u]:
                if (u, v) != e and (v, u) != e:
                    if not visit[v]:
                        dfs(v, e)
        edges.reverse()
        for u, v in edges:
            e = (u-1, v-1)
            visit = [0 for i in range(n)]
            dfs(0, e)
            c = sum(visit)
            if c == n:
                return [u, v]
        