# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1, next=head)
        left = dummy
        right = head

        while n:  # move the right pointer to desired start position
            right = right.next
            n -= 1
        while right:  # iterate till left reaches len - n position
            right = right.next
            left = left.next

        left.next = left.next.next  # node deletion
        return dummy.next