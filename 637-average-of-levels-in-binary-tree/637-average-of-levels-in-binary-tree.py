# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        vals = []
        
        queue = [root]
        while queue:
            _curr_vals = [_node.val for _node in queue]
            vals.append(sum(_curr_vals)/len(_curr_vals))
            
            for i in range(len(_curr_vals)):
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
            queue = queue[len(_curr_vals):]
            
        return vals
            