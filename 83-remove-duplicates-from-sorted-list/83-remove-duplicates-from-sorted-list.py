# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        prev = head
        _node = head.next
        while _node:
            if prev.val == _node.val:
                prev.next = _node.next
            else:
                prev = _node
            _node = _node.next

        return head