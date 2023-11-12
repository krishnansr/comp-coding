# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, next=head)
        _node = dummy
        while _node.next and _node.next.next:
            temp_next = _node.next  # assign 1 to temp_next
            _node.next = _node.next.next  # bring back 2

            temp_next.next = _node.next.next  # assign 3 after 1
            _node.next.next = temp_next  # move forward 1 after 2

            _node = _node.next.next  # iterate for nex pair
            
        return dummy.next