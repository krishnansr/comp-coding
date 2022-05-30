# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # get middle node
        fast_node = middle = head
        while fast_node and fast_node.next:
            middle = middle.next
            fast_node = fast_node.next.next

        # reverse second half of linked list
        tail = middle
        _node = middle.next
        while _node is not None:
            temp_next = _node.next
            _node.next = tail
            tail = _node
            _node = temp_next

        # compare from both ends for palindrome check
        while head != tail and head != middle:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next

        return True