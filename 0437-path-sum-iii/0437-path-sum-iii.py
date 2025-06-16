# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        ans = 0
        sums = [0]


        def trav(node, prevsum):
            nonlocal ans
            if not node:
                return

            currsum = prevsum+node.val
            print(sums)
            for summ in sums:
                if currsum-summ == targetSum:
                    ans += 1
            print(node.val, currsum, ans)

            sums.append(currsum)
            trav(node.left, currsum)
            trav(node.right, currsum)
            sums.pop()
        trav(root, 0)
        return ans
            
