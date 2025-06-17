# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        dc = {}

        def trav(node, path, d):
            nonlocal dc
            if not node: return

            if d not in dc:
                dc[d] = (node.val, path)
            
            if path > dc[d][1]:
                dc[d] = (node.val, path)

            trav(node.left, path+"l", d+1)
            trav(node.right, path+"r", d+1)

        # print(dc)
        ans = []
        trav(root, "", 0)
        for k in sorted(list(dc.keys())):
            ans.append(dc[k][0])

        return ans

            

        