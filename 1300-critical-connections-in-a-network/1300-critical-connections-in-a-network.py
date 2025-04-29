class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        graph = [[] for _ in range(n)]

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = [0]*n
        min_time = [float("inf")]*n
        time = [0]*n

        t = 0
        ans = []

        def dfs(u, parent):

            nonlocal t
            visit[u] = 1
            t+=1
            time[u] = t

            min_time[u] = time[u]
            
            for v in graph[u]:
                if v != parent:
                    if not visit[v]:
                        dfs(v, u)



            for v in graph[u]:
                if v != parent:
                    print("v time", v, min_time[v])
                    min_time[u] = min(min_time[u], min_time[v])


            for v in graph[u]:
                if v != parent:
                    if time[u] < min_time[v]:
                        ans.append([u, v])
        
        dfs(0, -1)

        print(time)
        print(min_time)

        return ans



        
        