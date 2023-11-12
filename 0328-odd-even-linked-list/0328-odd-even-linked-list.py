# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        even_head = ListNode(val=-1, next=None)
        even_node = even_head
        
        dummy = ListNode(val=-1, next=head)
        _node = dummy.next
        prev_node = None
        while _node and _node.next:
            temp_node = _node.next  # 2nd node
            _node.next = _node.next.next  # 1 -> 3

            temp_node.next = None   # 2 -> None
            even_node.next = temp_node
            even_node = even_node.next
            
            prev_node = _node
            _node =_node.next

        if _node is None:
            _node = prev_node

        if _node:
            _node.next = even_head.next  # attach even to odd list
        return dummy.next
