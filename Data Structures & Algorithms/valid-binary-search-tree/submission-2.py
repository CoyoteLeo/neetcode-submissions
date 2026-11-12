# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _isValidBST(node, min_v, max_v):
            if not node:
                return True

            if not min_v < node.val < max_v:
                return False

            return _isValidBST(node.left, min_v, node.val) and _isValidBST(node.right, node.val, max_v)
        

        return _isValidBST(root, -1000000001, 1000000001)