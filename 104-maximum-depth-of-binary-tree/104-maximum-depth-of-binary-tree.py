# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        max_depth = 0
        queue = [(root, 1)]
        while queue:
            _node, curr_depth = queue.pop(0)
            max_depth = max(max_depth, curr_depth)
            
            if _node.left:
                queue.append((_node.left, curr_depth + 1))
            if _node.right:
                queue.append((_node.right, curr_depth + 1))
        
        return max_depth