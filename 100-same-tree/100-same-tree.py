# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p == q
        
        p_stack = [p]
        q_stack = [q]
        while p_stack and q_stack:
            p_elem = p_stack.pop()
            q_elem = q_stack.pop()
            
            if p_elem.val != q_elem.val or \
                type(p_elem.left) != type(q_elem.left) or \
                type(p_elem.right) != type(q_elem.right):
                return False
            
            if p_elem.left:
                p_stack.append(p_elem.left)
            if p_elem.right:
                p_stack.append(p_elem.right)
            if q_elem.left:
                q_stack.append(q_elem.left)
            if q_elem.right:
                q_stack.append(q_elem.right)
        
        return len(p_stack) == len(q_stack)