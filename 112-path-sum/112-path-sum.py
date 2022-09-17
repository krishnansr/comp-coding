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
        if root.val == targetSum and not root.left and not root.right:
            return True
        
        new_target = targetSum - root.val
        return self.hasPathSum(root.left, new_target) or self.hasPathSum(root.right, new_target)
        
    
    def hasPathSum_nw(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        curr_sum = 0
        stack = []
        while stack:
            _node = stack[0]
            curr_sum += _node.val
            if curr_sum == targetSum:
                return True

            if _node.right:
                stack.insert(0, _node.right)
            if _node.left:
                stack.insert(0, _node.left)
            if _node.right is None and  _node.left is None:
                curr_sum -= _node.val
                stack.pop(0)