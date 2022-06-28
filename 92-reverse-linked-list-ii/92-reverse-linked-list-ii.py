# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1, next=head)
        ll, prev, i = None, None, 0

        _node = dummy
        while _node:
            if i > right:
                break

            elif i < left:
                ll = _node
                _node = _node.next
            
            else:  # left <= i <= right
                temp_next = _node.next
                _node.next = prev
                prev = _node
                _node = temp_next
            i += 1

        ll.next.next = _node  # set succesor to right of reversed list
        ll.next = prev  # set predecessor to left of reversed list
        return dummy.next