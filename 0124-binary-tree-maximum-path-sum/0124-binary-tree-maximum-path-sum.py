# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        dp = {}

        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                dp[node] = max(0, node.val)
            else:
                dp[node] = max(0, node.val+dfs(node.right), node.val+dfs(node.left))
            
            return dp[node]
        dfs(root)
        # print(list(zip([k.val for k in dp.keys()], dp.values())))
        maxi = float("-inf")
        def dfs2(node):
            nonlocal maxi
            if not node:
                return
            left = 0 if not node.left else dp[node.left]
            right = 0 if not node.right else dp[node.right]
            print(node.val, left, right)
            maxi = max(maxi, node.val + left + right)

            dfs2(node.left)
            dfs2(node.right)

        dfs2(root)
        return maxi



            

