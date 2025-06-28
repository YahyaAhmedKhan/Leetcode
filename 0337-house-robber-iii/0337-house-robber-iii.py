# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:


        dp = {}

        def mis(rootnode):
            if not rootnode: return 0
            if rootnode in dp:
                return dp[rootnode]

            notchoose = mis(rootnode.left)+mis(rootnode.right)

            choose = rootnode.val
            if rootnode.left:
                choose += mis(rootnode.left.right) + mis(rootnode.left.left)
            if rootnode.right:
                choose += mis(rootnode.right.right) + mis(rootnode.right.left)
            print(rootnode.val, choose, notchoose)
            dp[rootnode] = max(choose, notchoose)

            return dp[rootnode]

        ans =  mis(root)
        print(dp.values())
        return mis(root)
        