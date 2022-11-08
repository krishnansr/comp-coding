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
        _node = root
        while _node and _node.left:
            next_layer = _node.left
            prev_node = None
            while _node:
                _node.left.next = _node.right
                if prev_node:
                    prev_node.right.next = _node.left
                prev_node = _node
                _node = _node.next
            
            _node = next_layer
        return root
        
        
    def connect_bfs(self, root):
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