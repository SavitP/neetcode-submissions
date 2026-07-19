# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.swapChildren(root)
        return root

    def swapChildren(self, node: Optional[TreeNode]):
        if node is None:
            return
        temp = node.left
        node.left = node.right
        node.right = temp
        self.swapChildren(node.left)
        self.swapChildren(node.right)
        