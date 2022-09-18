# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs traversal
        if root is None:
            return 0

        level_node_counter = 1  # total number of nodes in a level
        level_counter = 0 # total number of levels
        stack = [root]
        while stack:
            _node = stack.pop(0)
            level_node_counter -= 1
            
            if _node.left:
                stack.append(_node.left)
            if _node.right:
                stack.append(_node.right)        

            if level_node_counter == 0:  # seen all nodes at current level
                level_counter += 1  # increase level count
                level_node_counter = len(stack)  # set num nodes count in next level
                
        return level_counter
    
    def maxDepth_rec(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # using recursion
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
                
    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        # dfs traversal
        if root is None:
            return 0
        
        max_depth = 0
        queue = [(root, 1)]
        while queue:
            _node, curr_depth = queue.pop()
            max_depth = max(max_depth, curr_depth)
            
            if _node.left:
                queue.append((_node.left, curr_depth + 1))
            if _node.right:
                queue.append((_node.right, curr_depth + 1))
        return max_depth