# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _node1 = head
        _node2 = head
        while _node1.next is not None:
            _node2 = _node2.next
            if _node1.next.next is None:
                break
            _node1 = _node1.next.next
        return _node2