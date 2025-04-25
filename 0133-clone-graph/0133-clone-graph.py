"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        dummy = Node(node.val)
        visit = {}
        nodes = {node.val: dummy}

        def dfs(u):
            if u.val in visit:
                return
            visit[u.val] = 1
            for v in u.neighbors:
                if v.val not in nodes:
                    nodes[v.val] = Node(v.val)
                nodes[u.val].neighbors.append(nodes[v.val])
                dfs(v)
        dfs(node)
        print(visit)
        print(nodes)
        return dummy

            


        