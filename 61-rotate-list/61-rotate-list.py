# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        _node = head
        while _node:
            size += 1
            _node = _node.next
        
        try:
            k %= size  # to avoid needless iterations, redcue k to {0, len}
            if k == 0:
                raise Exception
        except:
            # EAFP is better than LBYL paradigm
            return head
        
        # move fast node to (len-k)'th position
        _node = head
        fast_node = head
        for _ in range(k):
            fast_node = fast_node.next
            
        while fast_node and fast_node.next:
            fast_node = fast_node.next
            _node = _node.next
        
        # reorder list head and tail
        _node.next, fast_node.next, head = None, head, _node.next
        return head