# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ans = None

        def lca(node):
            nonlocal ans
            if not node: return 0

            curr = 1 if node in (p, q) else 0

            l, r = lca(node.left), lca(node.right)
            print(node.val, curr, l, r)


            if curr and (l or r):
                print("hi")
                ans = node
                return 2
            if l and r:
                ans = node
                return 2
            
            return curr+l+r

        lca(root)
        return ans



            





                