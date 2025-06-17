# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def find(node, val):
            if not node: return None

            if node.val == val:
                return node
            else:
                l, r = find(node.left, val), find(node.right, val)
                if l: return l
                # if r: return r
                return r
                return None

        return find(root, val)
        