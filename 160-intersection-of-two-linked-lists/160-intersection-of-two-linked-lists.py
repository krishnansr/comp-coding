# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # easy and creative solutions at https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/1093014/C++-Four-different-solutions
        # refer to the 3rd (length difference) and 4th (2-pointer) solutions specifically. Floyd's has same runtime but not as intuitive.
        _tailA = headA
        while _tailA.next:
            _tailA = _tailA.next
        
        # add a cycle to the first list and use floyd's cycle detection
        _tailA.next = headA

        # floyd's algorithm
        slow = fast = headB
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # no intersection
            _tailA.next = None
            return None
        
        # found an intersection, move to point of intersection
        fast = headB
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        # remove the artifically added cycle
        _tailA.next = None
        return slow
