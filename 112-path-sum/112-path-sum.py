# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        stack = [(root, 0)]
        while stack:
            _node, curr_val = stack.pop()
            if _node.val + curr_val == targetSum and not _node.left and not _node.right:
                return True
            
            if _node.left:
                stack.append((_node.left, _node.val + curr_val))
            if _node.right:
                stack.append((_node.right, _node.val + curr_val))
        
        return False
        
    def hasPathSum_rec(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        
        new_target = targetSum - root.val
        return self.hasPathSum(root.left, new_target) or \
               self.hasPathSum(root.right, new_target)
    
    