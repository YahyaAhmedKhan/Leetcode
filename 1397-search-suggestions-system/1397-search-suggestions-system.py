class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]  = Node(c)
            curr = curr.children[c]
        curr.isEnd = True
    
    def findthree(self, node, prefix):
        ans = []
        def dfs(currnode, path):
            if currnode.isEnd:
                if len(ans)==3:
                    return
                ans.append(path)
            
            for k in sorted(list(currnode.children.keys())):
                dfs(currnode.children[k], path+k)

        dfs(node, prefix)
        return ans



    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children: return []
            curr=curr.children[c]
        return self.findthree(curr, word)
    

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for p in products:
            trie.insert(p)
        ans = []
        pre = ""
        for c in searchWord:
            pre+=c
            ret = trie.search(pre)
            ans.append(ret)

        return ans
        