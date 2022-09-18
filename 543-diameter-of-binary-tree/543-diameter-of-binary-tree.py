# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # src explanation: https://youtu.be/bkxqA8Rfv04
        max_diameter = [0]
        
        def max_depth(root):
            if root is None:
                return -1
            
            # sol to https://leetcode.com/problems/maximum-depth-of-binary-tree/
            left_height = max_depth(root.left)
            right_height = max_depth(root.right)
            
            max_diameter[0] = max(max_diameter[0], left_height + right_height + 2)
            return 1 + max(left_height, right_height)
        
        max_depth(root)
        return max_diameter[0]