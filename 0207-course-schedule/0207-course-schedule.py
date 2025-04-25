class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        graph = [[] for i in range(numCourses)]

        pre = prerequisites
        for u, v in pre:
            graph[u].append(v)

        visit = [0 for _ in range(n)] 

        def dfs(u):
            if visit[u] == 2:
                return True

            if visit[u] == 1:
                return False
                
            visit[u] = 1

            ans = True
            for v in graph[u]:
                ans = dfs(v) and ans

            visit[u] = 2
            return ans

        ans = True
        for i in range(n):
            ans = ans and dfs(i)
        return ans
