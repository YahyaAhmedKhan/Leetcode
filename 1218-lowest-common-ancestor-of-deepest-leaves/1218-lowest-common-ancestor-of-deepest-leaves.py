# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def find_d(node):
            if not node: return -1
            return max(find_d(node.left), find_d(node.right)) + 1
        
        d  = find_d(root)
        c = 0
        def count(node, depth):
            nonlocal d, c
            if not node:
                return
            if depth < d:
                count(node.left, depth + 1)
                count(node.right, depth + 1)
                return
            if depth == d:
                c += 1
                return

        count(root, 0)
        ans = (-1, None)
        print(d, c)

        def helper(node, depth):
            nonlocal ans
            if not node: return 0
            if depth == d:
                val = 1
            else:
                val = helper(node.left, depth+1) + helper(node.right, depth+1)
            if val == c:
                ans = max ((depth, node), ans)
            
            return val
        helper(root, 0)
        return ans[1]



        helper(root, 0)
        return ans

            