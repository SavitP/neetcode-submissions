# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.createList([], 0, root)
    def createList(self, l, level, node):
        if node is None:
            return l
        if len(l) < level + 1:
            l.append([])
        l[level].append(node.val)
        l = self.createList(l, level + 1, node.left)
        l = self.createList(l, level + 1, node.right)
        return l
