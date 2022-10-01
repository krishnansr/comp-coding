# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        _node = slow
        prev = None
        while _node:
            temp_next = _node.next
            _node.next = prev
            prev = _node
            _node = temp_next

        _node = head
        while prev.next and _node.next:
            temp_next, prev_temp_next = _node.next, prev.next

            _node.next = prev
            prev.next = temp_next

            _node, prev = temp_next, prev_temp_next

        return head
