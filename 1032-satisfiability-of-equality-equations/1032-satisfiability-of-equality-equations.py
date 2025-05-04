class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, u):
        if self.par[u] == u:
            return u
        else:
            p = self.find(self.par[u])
            self.par[u] = p
            return p
        
    def merge(self, u, v):

        u, v = self.find(u), self.find(v)
        if u==v:
            return

        if self.rank[u]<self.rank[v]:
            self.par[u] = v
        elif self.rank[v]<self.rank[u]:
            self.par[v] = u
        else:
            self.par[u] = v
            self.rank[v]+=1

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        lets = set()
        nonEq = []
        eq = []
        for s in equations:
            lets.add(s[0])
            lets.add(s[3])
        dc = {}
    
        for i, u in enumerate(list(lets)):
            dc[u] = i


        for s in equations:
            if s[1] == "!":
                nonEq.append(( dc[s[0]], dc[s[3]]))
            else:
                eq.append(( dc[s[0]], dc[s[3]]))
        n = len(lets)
        dsu = UnionFind(n)
        for u, v in eq:
            if u!=v:
                dsu.merge(u, v)
        
        for u, v in nonEq:
            if dsu.find(u) == dsu.find(v):
                return False

        return True
            
        