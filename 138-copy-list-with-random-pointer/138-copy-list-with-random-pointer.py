"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # solution inspired from 
        # https://youtu.be/xbpUHSKoALg
        
        if not head:
            return None
        
        # step 1: interlearving new nodes
        _node = head
        while _node:
            _node.next = Node(_node.val, next=_node.next, random=None)
            _node = _node.next.next
        
        # step 2: assigning random ptrs
        _node = head
        while _node:
            _node.next.random = _node.random.next if _node.random else None
            _node = _node.next.next
            
        # step 3: splitting into two lists
        head = head.next
        _node = head
        while _node and _node.next:
            _node.next = _node.next.next
            _node = _node.next
            
        return head