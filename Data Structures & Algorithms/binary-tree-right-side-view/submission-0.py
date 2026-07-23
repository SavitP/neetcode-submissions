# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.explore(root, 1, 0, [])[0]

    def explore(self, node: Optional[TreeNode], height, max, l):
        if node is None:
            return [l, max]
        if height > max:
            l.append(node.val)
            max = height
        n = self.explore(node.right, height + 1, max, l)
        l = n[0]
        max = n[1]
        n = self.explore(node.left, height + 1, max, l)
        l = n[0]
        max = n[1]
        return [l, max]
