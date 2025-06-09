class Node:
    def __init__(self, val: int, c=None):
        assert isinstance(val, int)
        self.val = val
        self.children = c if c else []
    
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        root = Node(-1, [Node(i) for i in range(1, min(10, n+1))])
        
        dq = deque()
        for c in root.children: dq.append(c)

        flag = False
        while True:
            curr = dq.popleft()
            for i in range(10):
                
                newval = curr.val*10+i

                if newval<=n:
                    newnode = Node(newval)
                    curr.children.append(newnode)
                    dq.append(newnode)

                else: flag=True

            if flag: break

        # print(root.children[0].children[0].val)
        
        ans = []
        def dfs(root):
            if root.val!=-1:
                ans.append(root.val)
            for i in root.children:
                dfs(i)
        dfs(root)
        return ans

