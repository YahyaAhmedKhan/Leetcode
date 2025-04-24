class UnionFind:

    def __init__(self, n):
        self.parent  = [i for i in range(n)]
        self.rank  = [0 for i in range(n)]
        self.comps = n
    
    def find(self, u):
        if self.parent[u] == u:
            return u
        else:
            par = self.find(self.parent[u])
            self.parent[u] = par
            return par
    
    def merge(self, u, v):
        par_u = self.find(u)
        par_v = self.find(v)
        if par_u == par_v:
            return 
        else:
            if self.rank[par_u] > self.rank[par_v]:
                self.parent[par_v] = par_u
            elif self.rank[par_v] > self.rank[par_u]:
                self.parent[par_u] = par_v
            else:
                self.rank[par_u] += 1
                self.parent[par_v] = par_u
            self.comps -=1
            return
            
        


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    uf.merge(i, j)
        
        return uf.comps

        