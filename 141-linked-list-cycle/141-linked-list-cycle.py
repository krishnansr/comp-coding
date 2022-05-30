# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        max_val = 100000
        _node = head
        while _node:
            if _node.val > max_val:
                return True
            _node.val += 2 * max_val
            _node = _node.next
            
        return False