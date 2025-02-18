# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        a, b = [], []
        def prleft(node):
            if (not node):
                a.append('0')
                return
            a.append(node.val)
            prleft(node.left)
            prleft(node.right)

        def prright(node):
            if (not node):
                b.append('0')
                return
            b.append(node.val)
            prright(node.right)
            prright(node.left)
            
        
        prright(root)
        prleft(root)
        # print(a)
        # print(b)

        return a == b
