# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def trav(root, maxi):
            nonlocal ans

            if not root: return
            if maxi <= root.val:
                ans+=1

            maxi = max (maxi, root.val)
            trav(root.left, maxi)
            trav(root.right, maxi)
        trav(root, float("-inf"))
        return ans


        