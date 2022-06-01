# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        all_nodes = []
        _node = head
        while _node:
            all_nodes.append(_node)
            _node = _node.next
        all_nodes.append(None)

        if n + 1 == len(all_nodes):
            head = head.next
        else:
            all_nodes[len(all_nodes) - n - 2].next = all_nodes[len(all_nodes) -n]
        return head