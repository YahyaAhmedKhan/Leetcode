class Node():
    def __init__(self, val = None):
        self.val = val
        self.children = {}
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        if len(word)==0:
            self.root.isEnd = True
            return

        curr_node = self.root
        i = 0
        while i<len(word) and (word[i] in curr_node.children):
            curr_node = curr_node.children[word[i]]
            i+=1
        
        while i<len(word):
            new_node = Node(word[i])
            curr_node.children[word[i]] = new_node
            curr_node = new_node
            i+=1
        
        curr_node.isEnd = True


    def search(self, word: str) -> bool:
        curr_node = self.root
        i = 0
        while (i<len(word) and word[i] in curr_node.children):
            curr_node = curr_node.children[word[i]]
            i+=1
        
        return i==len(word) and curr_node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        i = 0
        while (i<len(prefix) and prefix[i] in curr_node.children):
            curr_node = curr_node.children[prefix[i]]
            i+=1
        
        return i==len(prefix)

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)