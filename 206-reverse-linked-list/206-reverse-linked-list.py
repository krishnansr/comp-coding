# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        _node = head
        while _node is not None:
            temp_next = _node.next
            _node.next = prev
            prev = _node
            _node = temp_next
        
        head = prev
        return head
    
    def reverseList_recursive(self, node: Optional[ListNode]) -> Optional[ListNode]:
        # for understadning recusive reversal: 
        # https://www.youtube.com/watch?v=MRe3UsRadKw
        if node is None or node.next is None:
            return node
        
        node1 = self.reverseList_recursive(node.next)
        node.next.next = node
        node.next = None
        return node1
    