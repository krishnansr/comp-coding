"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return root
        
        queue = [(root, 0)]
        while queue:
            _node, _level = queue.pop(0)
            _node.next = queue[0][0] if queue and queue[0][1] == _level else None
            
            if _node.left:
                queue.append((_node.left, _level + 1))
            if _node.right:
                queue.append((_node.right, _level + 1))

        return root