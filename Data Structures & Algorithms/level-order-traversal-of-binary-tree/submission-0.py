# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def bfs(idx, node):
            if not node:
                return

            if idx == len(ans):
                ans.append([])
            ans[idx].append(node.val)
            bfs(idx + 1, node.left)
            bfs(idx + 1, node.right)
        bfs(0, root)
        return ans