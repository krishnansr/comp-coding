# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(val=-1, next=None)
        res = dummy
        carry = 0
        while l1 or l2:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            
            _sum = digit1 + digit2 + carry
            carry, digit = _sum // 10, _sum % 10
            
            # update l1
            res.next = ListNode(val=digit, next=None)
            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            res.next = ListNode(val=1)
        return dummy.next