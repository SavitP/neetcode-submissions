# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.find(root, -101, 0)
    
    def find(self, node: TreeNode, max, count):
        if node is None:
            return 0
        add = 0
        if node.val >= max:
            add += 1
            max = node.val
        count = self.find(node.left, max, count) + self.find(node.right, max, count) + add
        return count