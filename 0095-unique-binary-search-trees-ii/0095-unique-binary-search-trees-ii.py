# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dupli(root, offset):
            if not root: return None
            curr = TreeNode(root.val+offset)

            curr.left = dupli(root.left, offset)
            curr.right = dupli(root.right, offset)
            return curr

        dp = [[] for _ in range(n+1)]
        dp[0].append(None)
        dp[1].append(TreeNode(1))

        for nodes in range(2, n+1):
            for root in range(1, nodes+1):
                for lefttree in dp[root-1]:
                    for rightroot in dp[nodes-root]:
                        righttree = dupli(rightroot, root)
                        newroot = TreeNode(root)
                        newroot.left = lefttree
                        newroot.right = righttree

                        dp[nodes].append(newroot)

        return dp[n]


        