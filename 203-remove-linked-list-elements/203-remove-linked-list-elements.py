# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev_node = None
        _node = head
        while _node is not None:
            if _node.val == val:
                if _node == head:  # handle head separately
                    head = _node.next
                else:
                    prev_node.next = _node.next
            else:
                prev_node = _node  # update previous node only when no nodes are deleted
            _node = _node.next
        return head