# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_a = 1
        _nodeA = headA
        while _nodeA.next:
            _nodeA = _nodeA.next
            len_a += 1
            
        len_b = 1
        _nodeB = headB
        while _nodeB.next:
            _nodeB = _nodeB.next
            len_b += 1
            
        # check if there is an intersection - usually last nodes are same
        if _nodeA != _nodeB:
            return None
                
        # add a cycle to the longer list and use floyd's cycle detection
        if len_a > len_b:
            mod_node, mod_node.next, alt_head = _nodeA, headA, headB 
        else:
            mod_node, mod_node.next, alt_head = _nodeB, headB, headA

        # floyd's algorithm
        fast = alt_head
        slow = alt_head
        while True:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        while alt_head != slow:
            alt_head = alt_head.next
            slow = slow.next
            
        # remove the artifically added cycle
        mod_node.next = None
        return slow