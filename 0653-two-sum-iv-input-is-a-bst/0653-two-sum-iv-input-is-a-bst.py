# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        
        subtrahend_set = set()
        queue = [root]
        while queue:
            node = queue.pop(0)  # BFS
            
            if k - node.val in subtrahend_set:
                return True
            subtrahend_set.add(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return False