class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = set()
        for u, v in equations:
            nodes.add(u)
            nodes.add(v)

        n = len(nodes)
        graph = {v:[] for v in list(nodes)}

        for i in range(len(equations)):
            u, v = equations[i]
            d = values[i]

            graph[u].append((v, d))
            graph[v].append((u, (1.0/d)))

        visit = {v:0 for v in list(nodes)}

        def find(u, v, result):
            if u not in nodes or v not in nodes:
                return -1.0
            if u == v: return 1.0
            visit[u]=1
            for k, d in graph[u]:
                if k==v:
                    return result*d
                if not visit[k]:
                    ans = find(k, v, result*d)
                    if ans>=0:
                        print("ret ", ans)
                        return ans
            return -1.0

        answers = []
        for i in queries:
            visit = {v:0 for v in list(nodes)}
            u, v = i
            ans = find(u, v, 1)
            answers.append(ans)
        # for i in list(graph.keys()):
        #     print(i, end= " ")
        #     print(graph[i])
        return answers


            

