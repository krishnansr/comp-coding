# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        min_depth = 0
        
        queue = [root]
        while queue:
            for _ in range(len(queue)):
                elem = queue.pop(0)
                if elem != root and elem.left is None and elem.right is None:
                    return min_depth + 1
                
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
            min_depth += 1
            
        return min_depth