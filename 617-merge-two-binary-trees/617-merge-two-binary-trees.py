# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if None in [root1, root2]:
            return root1 if root1 else root2

        _node = TreeNode(val=root1.val + root2.val)
        _node.left = self.mergeTrees(root1.left, root2.left)
        _node.right = self.mergeTrees(root1.right, root2.right)    
        return _node