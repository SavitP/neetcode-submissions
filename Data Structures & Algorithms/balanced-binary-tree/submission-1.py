# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def h(node: Optional[TreeNode]):
            if not node:
                return [True, 0]
            l1 = h(node.left)
            if l1[0] == False:
                return [False, 0]
            l2 = h(node.right)
            if l2[0] == False or abs(l1[1] - l2[1]) > 1:
                return [False, 0]
            return [True, max(l1[1], l2[1]) + 1]
        return h(root)[0]
            
    