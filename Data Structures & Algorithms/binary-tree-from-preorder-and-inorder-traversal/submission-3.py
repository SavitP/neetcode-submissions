# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, inorder)[0]
    
    def build(self, preorder, inorder):
        if len(inorder) == 0:
            return [None, preorder]
        node = TreeNode(preorder[0])
        # Remove stuff from preorder list before calling right
        i = inorder.index(preorder[0])
        preorder = preorder[1:]
        l = self.build(preorder, inorder[:i])
        node.left = l[0]
        r = self.build(l[1], inorder[i+1:])
        node.right = r[0]
        return [node, r[1]]