# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.good(root, -1001, 1001)
    def good(self, node: Optional[TreeNode], min, max):
        if node is None:
            return True
        if node.val <= min or node.val >= max:
            return False
        return self.good(node.left, min, node.val) and self.good(node.right, node.val, max)