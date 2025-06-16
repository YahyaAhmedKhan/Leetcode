# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def trav(node, currlen, fromright):
            nonlocal ans
            if not node: return

            ans = max(ans, currlen)
            print(node.val, currlen, "r" if fromright else "l")
            if fromright:
                trav(node.left, currlen+1, False)
                trav(node.right, 1, True)
            else: # from left
                trav(node.left, 1, False)
                trav(node.right, currlen+1, True)


        trav(root, 0, True)
        trav(root, 0, False)

        return ans







