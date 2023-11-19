# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder traversal must be sorted.
        def inorder_traversal(node):
            if node:
                yield from inorder_traversal(node.left)
                yield node.val
                yield from inorder_traversal(node.right)
        
        prev_val = float('-inf')
        for val in inorder_traversal(root):
            if val <= prev_val:
                return False
            prev_val = val
        return True