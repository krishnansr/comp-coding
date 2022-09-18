# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if None in [root, subRoot]:
            return root == subRoot
        
        def is_match(n1, n2):
            if None in [n1, n2]:
                return n1 == n2
            return n1.val == n2.val and \
                    is_match(n1.left, n2.left) and \
                    is_match(n1.right, n2.right)
        
        return is_match(root, subRoot) or \
                self.isSubtree(root.left, subRoot) or \
                self.isSubtree(root.right, subRoot)