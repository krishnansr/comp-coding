# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head

        if head.val == val:
            return self.removeElements(head.next, val)

        prev_node = head
        _node = head.next
        while _node is not None:
            if _node.val == val:
                prev_node.next = _node.next
            else:
                prev_node = _node
            _node = _node.next
        return head